import logging
from datetime import datetime, time
from database.models import Programs, User, UserFavorite, Donation
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text, and_, update, func


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def add_channel_program(session: AsyncSession, channel_name, program_data):
    if not program_data:
        logger.error(f"Программы для канала {channel_name} отсутствуют.")
        return

    for time_str, title in program_data:
        try:
            logger.info(f"Добавление программы для канала {channel_name}: {time_str} - {title}")
            time_obj = datetime.strptime(time_str, '%H:%M').time()
            insert_stmt = Programs.__table__.insert().values(
                channel_name=channel_name,
                program_time=time_obj,
                program_title=title
            )
            await session.execute(insert_stmt)
        except Exception as e:
            logger.error(f"Ошибка вставки программы для {channel_name}: {e}")

    logger.info(f"Коммит транзакции для канала {channel_name}")
    await session.commit()


async def orm_get_programs(session: AsyncSession, channel_name: str):
    # Получаем текущее время и дату
    current_time = datetime.now().time()
    current_date = datetime.now().date()

    # Запрос для программ сегодняшнего дня (с 05:00 до 23:59)
    query_today = (
        select(Programs)
        .where(
            and_(
                Programs.channel_name == channel_name,
                Programs.program_time >= time(5, 0),
                Programs.program_time <= time(23, 59)
            )
        )
        .order_by(Programs.program_time)
    )

    # Запрос для программ следующего дня (с 00:00 до 04:59)
    query_tomorrow = (
        select(Programs)
        .where(
            and_(
                Programs.channel_name == channel_name,
                Programs.program_time >= time(0, 0),
                Programs.program_time <= time(4, 59)
            )
        )
        .order_by(Programs.program_time)
    )

    # Запрос для программ вчерашнего вечера (с 22:00 до 23:59)
    query_yesterday_late_night = (
        select(Programs)
        .where(
            and_(
                Programs.channel_name == channel_name,
                Programs.program_time >= time(22, 0),
                Programs.program_time <= time(23, 59)
            )
        )
        .order_by(Programs.program_time)
    )

    # Выполняем запросы
    result_today = await session.execute(query_today)
    result_tomorrow = await session.execute(query_tomorrow)
    result_yesterday_late_night = await session.execute(query_yesterday_late_night)

    # Получаем результаты
    programs_today = result_today.scalars().all()
    programs_tomorrow = result_tomorrow.scalars().all()
    programs_yesterday_late_night = result_yesterday_late_night.scalars().all()

    # Список предстоящих программ и текущая программа
    upcoming_programs = []
    current_program = None

    # Проверка времени, чтобы включить текущую программу
    if current_time < time(5, 0):
        # Время после полуночи до 05:00
        if programs_yesterday_late_night:
            # Берем последнюю программу из вчерашнего вечера
            last_night_program = programs_yesterday_late_night[-1]
            # Если следующая программа еще не началась, значит текущая - вчерашняя
            if not programs_tomorrow or (programs_tomorrow and programs_tomorrow[0].program_time > current_time):
                current_program = last_night_program

        # Добавляем программы текущего дня
        if current_program:
            upcoming_programs.append(current_program)
        upcoming_programs.extend(programs_tomorrow)

    else:
        # Время после 05:00 - ищем текущую программу в сегодняшнем расписании
        for program in programs_today:
            if program.program_time <= current_time:
                current_program = program
            elif program.program_time > current_time:
                upcoming_programs.append(program)

        # Вставляем текущую программу, если она найдена
        if current_program:
            upcoming_programs.insert(0, current_program)

        # Добавляем завтрашние программы (с 00:00 до 04:59)
        upcoming_programs.extend(programs_tomorrow)

    return upcoming_programs


async def orm_get_program(session: AsyncSession, program_title: str):
    query = select(Programs).where(Programs.channel_name == program_title)
    result = await session.execute(query)
    return result.scalar()


async def orm_delete_all_programs(session: AsyncSession):
    try:
        # Удаляем все записи из таблицы программ
        await session.execute(text("DELETE FROM tvprograms"))
        await session.commit()
        print("Все программы удалены успешно.")
    except Exception as e:
        print(f"Ошибка при удалении всех программ: {e}")
        await session.rollback()


async def add_new_user(session: AsyncSession, user_id: str, username: str):
    # Проверяем, есть ли пользователь в базе
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    user = result.scalars().first()

    # Если пользователь новый, добавляем его в базу
    if not user:
        new_user = User(user_id=user_id, username=username)
        session.add(new_user)
        await session.commit()
        return new_user
    return user  # Возвращаем объект пользователя, если он уже существует


async def add_favorite_channel(session: AsyncSession, user_id: str, channel_name: str):
    # Получаем пользователя по user_id
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    user = result.scalars().first()

    # Если пользователь не найден, сначала добавляем его
    if not user:
        raise ValueError("User not found. Please register the user before adding favorites.")

    # Проверяем, есть ли уже канал в избранном
    query_fav = select(UserFavorite).where(
        UserFavorite.user_id == user.id,
        UserFavorite.channel_name == channel_name
    )
    result_fav = await session.execute(query_fav)
    favorite = result_fav.scalars().first()

    # Если канал еще не в избранном, добавляем
    if not favorite:
        new_favorite = UserFavorite(user_id=user.id, channel_name=channel_name)
        session.add(new_favorite)
        await session.commit()
        return new_favorite
    return favorite  # Если уже есть, возвращаем существующий объект


# ORM-методы для работы с избранным
async def orm_add_to_favorites(session: AsyncSession, user_id: str, channel_name: str):
    result = await session.execute(
        select(UserFavorite).where(UserFavorite.user_id == user_id, UserFavorite.channel_name == channel_name)
    )
    favorite = result.scalars().first()
    if not favorite:
        new_favorite = UserFavorite(user_id=user_id, channel_name=channel_name, created=datetime.now())
        session.add(new_favorite)
        await session.commit()


async def orm_remove_from_favorites(session: AsyncSession, user_id: str, channel_name: str):
    result = await session.execute(
        select(UserFavorite).where(UserFavorite.user_id == user_id, UserFavorite.channel_name == channel_name)
    )
    favorite = result.scalars().first()
    if favorite:
        await session.delete(favorite)
        await session.commit()


async def orm_get_favorites(session: AsyncSession, user_id: str):
    result = await session.execute(
        select(UserFavorite).where(UserFavorite.user_id == str(user_id))  # Приведение user_id к строке
    )
    return result.scalars().all()


async def ensure_user_exists(user_id: str, session: AsyncSession) -> bool:
    """Проверка существования пользователя"""
    user_id_str = str(user_id)
    query = select(User).where(User.user_id == user_id_str)
    result = await session.execute(query)
    return result.scalar_one_or_none() is not None


async def save_donation(session: AsyncSession, user_id: str, amount: int, payment_id: str) -> None:
    """Сохраняет информацию о донате через Telegram Stars"""
    donation = Donation(
        user_id=str(user_id),
        amount=amount,
        payment_id=payment_id
    )
    session.add(donation)
    await session.commit()


async def get_user_total_donations(session: AsyncSession, user_id: str) -> int:
    """Возвращает общую сумму донатов пользователя в звездах"""
    result = await session.execute(
        select(func.sum(Donation.amount))
        .where(Donation.user_id == str(user_id))
    )
    total = result.scalar()
    return total or 0


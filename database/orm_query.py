import logging
from database.models import Programs
from datetime import datetime, time, timedelta
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, text, insert, values, update, delete, func, and_, or_


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


async def orm_get_programs(session: AsyncSession, channel_name):
    # Получаем текущее время
    current_time = datetime.now().time()

    # Запрос для получения всех программ на текущий день (от начала дня до конца)
    query_today = (
        select(Programs)
        .where(
            and_(
                Programs.channel_name == channel_name,
                Programs.program_time >= time(0, 0),  # Программы с начала дня
                Programs.program_time <= time(23, 59)  # До конца дня
            )
        )
        .order_by(Programs.program_time)  # Сортировка по времени программы
    )

    # Запрос для получения программ на следующий день (с полуночи до 05:00)
    query_tomorrow = (
        select(Programs)
        .where(
            and_(
                Programs.channel_name == channel_name,
                Programs.program_time >= time(0, 0),  # Программы с полуночи
                Programs.program_time <= time(5, 0)   # До 05:00
            )
        )
        .order_by(Programs.program_time)  # Сортировка по времени программы
    )

    # Выполняем оба запроса
    result_today = await session.execute(query_today)
    result_tomorrow = await session.execute(query_tomorrow)

    # Получаем списки программ
    programs_today = result_today.scalars().all()
    programs_tomorrow = result_tomorrow.scalars().all()

    # Найдем текущую программу (которая идет в данный момент)
    current_program = None
    upcoming_programs = []

    for i, program in enumerate(programs_today):
        # Если нашли программу, которая идет сейчас
        if program.program_time <= current_time:
            if i + 1 < len(programs_today):
                next_program = programs_today[i + 1]
                # Если следующая программа начинается после текущего времени, значит текущая программа идет сейчас
                if next_program.program_time > current_time:
                    current_program = program
                    upcoming_programs = programs_today[i + 1:]
                    break
            else:
                # Если это последняя программа на сегодня
                current_program = program
                break

    # Если программа найдена, добавляем ее в результат
    if current_program:
        upcoming_programs.insert(0, current_program)

    # Добавляем программы на следующий день (после полуночи)
    upcoming_programs += programs_tomorrow

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


# async def orm_add_program(session: AsyncSession):
#     obj = Programs(
#         channel_name = 'Первый канал',
#         program_title = 'Футбол',
#         program_time = time(16,55)
#     )
#     session.add(obj)
#     await session.commit()



# async def add_channel_program(session, channel_name, program_data):
#     for time_str, title in program_data:
#         time_obj = datetime.strptime(time_str, '%H:%M').time()
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name=channel_name,
#             program_time=time_obj,
#             program_title=title
#         )
#         await session.execute(insert_stmt)
#     await session.commit()



# async def add_first_channel_program(session: AsyncSession):
#     channel_name = "Первый канал"  # Или любой другой источник данных для имени канала

#     for time_str, title in first_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Первый канал',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_russia_one_channel_program(session: AsyncSession):
#     channel_name = "Россия 1"  # Или любой другой источник данных для имени канала

#     for time_str, title in russia_one_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Россия 1',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_match_tv_channel_program(session: AsyncSession):
#     channel_name = "Матч"  # Или любой другой источник данных для имени канала

#     for time_str, title in match_tv_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Матч',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_ntv_channel_program(session: AsyncSession):
#     channel_name = "НТВ"  # Или любой другой источник данных для имени канала

#     for time_str, title in ntv_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='НТВ',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_five_tv_channel_program(session: AsyncSession):
#     channel_name = "Пятый"  # Или любой другой источник данных для имени канала

#     for time_str, title in five_tv_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Пятый',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_tv_center_channel_program(session: AsyncSession):
#     channel_name = "ТВ Центр"  # Или любой другой источник данных для имени канала

#     for time_str, title in tv_center_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='ТВ Центр',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_culture_channel_program(session: AsyncSession):
#     channel_name = "Культура"  # Или любой другой источник данных для имени канала

#     for time_str, title in culture_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Культура',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_sts_channel_program(session: AsyncSession):
#     channel_name = "СТС"  # Или любой другой источник данных для имени канала

#     for time_str, title in sts_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='СТС',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_ren_tv_channel_program(session: AsyncSession):
#     channel_name = "РЕН ТВ"  # Или любой другой источник данных для имени канала

#     for time_str, title in ren_tv_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='РЕН ТВ',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_otp_channel_program(session: AsyncSession):
#     channel_name = "ОТР"  # Или любой другой источник данных для имени канала

#     for time_str, title in otp_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='ОТР',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_tnt_channel_program(session: AsyncSession):
#     channel_name = "ТНТ"  # Или любой другой источник данных для имени канала

#     for time_str, title in tnt_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='ТНТ',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_home_channel_program(session: AsyncSession):
#     channel_name = "Домашний"  # Или любой другой источник данных для имени канала

#     for time_str, title in home_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Домашний',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_friday_channel_program(session: AsyncSession):
#     channel_name = "Пятница"  # Или любой другой источник данных для имени канала

#     for time_str, title in friday_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Пятница',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_tv3_channel_program(session: AsyncSession):
#     channel_name = "ТВ-3"  # Или любой другой источник данных для имени канала

#     for time_str, title in tv3_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='ТВ-3',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_muz_tv_channel_program(session: AsyncSession):
#     channel_name = "МУЗ ТВ"  # Или любой другой источник данных для имени канала

#     for time_str, title in muz_tv_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='МУЗ ТВ',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_carousel_channel_program(session: AsyncSession):
#     channel_name = "Карусель"  # Или любой другой источник данных для имени канала

#     for time_str, title in carousel_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Карусель',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_star_channel_program(session: AsyncSession):
#     channel_name = "Звезда"  # Или любой другой источник данных для имени канала

#     for time_str, title in star_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Звезда',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_che_channel_program(session: AsyncSession):
#     channel_name = "Че"  # Или любой другой источник данных для имени канала

#     for time_str, title in che_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Че',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_mir_channel_program(session: AsyncSession):
#     channel_name = "МИР"  # Или любой другой источник данных для имени канала

#     for time_str, title in mir_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='МИР',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_spas_channel_program(session: AsyncSession):
#     channel_name = "Спас ТВ"  # Или любой другой источник данных для имени канала

#     for time_str, title in spas_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Спас ТВ',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_you_channel_program(session: AsyncSession):
#     channel_name = "Ю"  # Или любой другой источник данных для имени канала

#     for time_str, title in you_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Ю',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()


# async def add_russia24_channel_program(session: AsyncSession):
#     channel_name = "Россия 24"  # Или любой другой источник данных для имени канала

#     for time_str, title in russia24_channel_program_data:
#         # Преобразуем строку времени в объект времени
#         time_obj = datetime.strptime(time_str, '%H:%M').time()

#         # Собираем запрос на вставку данных
#         insert_stmt = Programs.__table__.insert().values(
#             channel_name='Россия 24',  # Добавляем значение для channel_name
#             program_time=time_obj,
#             program_title=title
#         )

#         # Выполняем запрос
#         await session.execute(insert_stmt)

#     # Подтверждаем транзакцию
#     await session.commit()

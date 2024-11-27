import logging
from datetime import datetime
from functools import partial
from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager, Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Cancel, Row, Url, Button
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.orm_query import orm_get_programs, orm_add_to_favorites, orm_remove_from_favorites, orm_get_favorites
from database.models import User


# Словарь с URL для каждого канала
channel_urls = {
    "Первый канал": "https://www.1tv.com/live",
    "Россия 1": "https://vgtrk.ru/russiatv",
    "Матч": "https://matchtv.ru/channel/matchtv",
    "НТВ": "https://www.ntv.ru/air/ntv",
    "Пятый": "https://www.5-tv.ru/live/",
    "ТВ Центр": "https://www.ntv.ru/air/tvc",
    "Культура": "https://vgtrk.ru/tvkultura",
    "РЕН ТВ": "https://www.ntv.ru/air/rentv",
    "ОТР": "https://otr-online.ru/online/",
    "ТНТ": "https://tnt-online.ru/live",
    "СТС": "https://ctc.ru/online/",
    "Домашний": "https://domashniy.ru/online",
    "Пятница": "https://friday.ru/live",
    "ТВ-3": "https://tv3.ru/live",
    "МУЗ ТВ": "https://muz-tv.ru/online/",
    "Карусель": "https://www.ntv.ru/air/carusel",
    "Звезда": "https://tvzvezda.ru/video",
    "Че": "https://chetv.ru/online",
    "МИР": "https://www.ntv.ru/air/mir",
    "Спас ТВ": "https://spastv.ru/efir/",
    "Ю": "https://www.u-tv.ru/online/",
    "Россия 24": "https://vgtrk.ru/russia24",
    "viju TV1000": "https://viju.ru/tv-channels/viju-tv1000/",
    "viju TV1000 русское": "https://viju.ru/tv-channels/viju-tv1000-russkoe/",
    "viju TV1000 action": "https://viju.ru/tv-channels/viju-tv1000-action/",
    "viju+ Comedy": "https://viju.ru/tv-channels/vijuplus-comedy/",
    "viju+ Megahit": "https://viju.ru/tv-channels/vijuplus-megahit/",
    "viju+ Premiere": "https://viju.ru/tv-channels/vijuplus-premiere/",
    "viju+ Serial": "https://viju.ru/tv-channels/vijuplus-serial/",
    "viju Explore": "https://viju.ru/tv-channels/viju-explore/",
    "viju History": "https://viju.ru/tv-channels/viju-history/",
    "viju Nature": "https://viju.ru/tv-channels/viju-nature/",
    "Нано": "https://tv-nano.ru/",
    "МАТЧ! Футбол 3": "https://matchtv.ru/channel/futbol-3",
    "МАТЧ! Боец": "https://matchtv.ru/channel/boec",
    "Футбол": "https://football-tv.ru/live",
    "viju+ Sport": "https://viju.ru/tv-channels/vijuplus-sport/",
    "МАТЧ! Футбол 1": "https://matchtv.ru/channel/futbol-1",
    "МАТЧ! Футбол 2": "https://matchtv.ru/channel/futbol-2",
    "МАТЧ! Арена": "https://matchtv.ru/channel/arena",
    "МАТЧ! Игра": "https://matchtv.ru/channel/igra",
    "МАТЧ! Премьер": "https://matchpremier.ru/live",
    "МАТЧ! Страна": "https://matchtv.ru/channel/strana",
    "Старт Триумф": "https://tvstart.ru/schedule/start-triumph/",
    "МИР 24": "https://onair.mir24.tv/",
    "360° Новости": "https://360.ru/streams/",
    "Al JaZeera": "https://www.aljazeera.com/live",
    "Ru.TV": "https://ru.tv/watch/online",
    "BRIDGE TV": "https://bridgetv.ru/",
    "SONGTV Russia": "https://songtv.ru/live",
    "Fashion TV": "https://fashiontv.ru/live",
    "СТС Love": "https://ctclove.ru/online",
    "Суббота!": "https://subbota.tv/"
}


async def add_new_user_if_not_exists(session: AsyncSession, user_id: str, username: str):
    # Проверка на наличие пользователя
    result = await session.execute(select(User).where(User.user_id == user_id))
    user = result.scalars().first()

    if user:
        # Обновляем поле updated_at для существующего пользователя
        user.updated = datetime.now()
        session.add(user)  # Убедитесь, что объект добавлен в сессию
        logging.info(f"Обновлено поле 'updated' для пользователя {user_id}")
    else:
        # Создаем нового пользователя, если его нет в базе
        new_user = User(user_id=user_id, username=username, created=datetime.now(), updated=datetime.now())
        session.add(new_user)
        logging.info(f"Добавлен новый пользователь {user_id}")

    # Фиксируем изменения в базе
    logging.info(f"Пользователь найден: {user}, обновляем updated.")
    await session.commit()
    logging.info("Изменения зафиксированы в базе данных.")


async def get_tv_program(dialog_manager: DialogManager, event_from_user, session: AsyncSession, channel_name: str, **kwargs):
    # Добавление пользователя, если его нет в базе
    await add_new_user_if_not_exists(session, user_id=str(event_from_user.id), username=event_from_user.username)

    # Получение списка программ для указанного канала
    res = await orm_get_programs(session, channel_name)
    if res:
        res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
    else:
        res = 'Нет программ на оставшуюся часть дня.'
    return {'program_title': res}


def create_tv_channel_dialog(channel_name: str, state) -> Dialog:

    url = channel_urls.get(channel_name)  # Получаем URL для канала (None, если нет)

    # Функции для обработки действий с избранным
    add_to_favorites_handler = partial(add_to_favorites, channel_name=channel_name)
    remove_from_favorites_handler = partial(remove_from_favorites, channel_name=channel_name)

    # Кнопки для избранного
    buttons_favorites = [
        Button(Const('➕ Добавить в ❤️'), id='add_to_favorites', on_click=add_to_favorites_handler, when="not_in_favorites"),
        Button(Const('➖ Убрать из ❤️'), id='remove_from_favorites', on_click=remove_from_favorites_handler, when="in_favorites"),
    ]

    # Если есть URL
    if url:
        # Ряд с кнопкой "Смотреть online" и кнопками избранного
        buttons_top_row = [
            Url(Const('Смотреть online'), url=Const(url))
        ]
        buttons_bottom_row = [
            Cancel(Const('◀️ Назад'), id='b_cancel'),  # Кнопка "Назад" на отдельной строке
            *buttons_favorites
        ]
    else:
        # Если нет URL, то кнопки для избранного и кнопка "Назад" в одном ряду
        buttons_top_row = [
            Cancel(Const('◀️ Назад'), id='b_cancel'),  # Кнопка "Назад"
            *buttons_favorites,  # Кнопки "Добавить в избранное" и "Убрать из избранного"
        ]
        buttons_bottom_row = []

    return Dialog(
        Window(
            Const(f'⭐️ <b>Программа передач</b> ⭐️\n\n📺 <b>{channel_name}</b>\n'),
            Format('{program_title}'),
            Row(*buttons_top_row),  # Вставляем кнопки в верхний ряд
            *[Row(*buttons_bottom_row)] if buttons_bottom_row else [],  # Вставляем нижний ряд только если есть
            getter=lambda dialog_manager, event_from_user, session, **kwargs: get_tv_program_with_favorite_status(
                dialog_manager, event_from_user, session, channel_name
            ),
            state=state,
        ),
    )


# Обновленный handler для кнопок
async def add_to_favorites(callback: CallbackQuery, button: Button, manager: DialogManager, channel_name: str, **kwargs):
    session = manager.middleware_data['session']
    user_id = str(callback.from_user.id)

    await orm_add_to_favorites(session, user_id, channel_name)
    # Обновляем интерфейс с передачей текущих данных
    await manager.update(data={})


async def remove_from_favorites(callback: CallbackQuery, button: Button, manager: DialogManager, channel_name: str, **kwargs):
    session = manager.middleware_data['session']
    user_id = str(callback.from_user.id)

    await orm_remove_from_favorites(session, user_id, channel_name)
    # Обновляем интерфейс с передачей текущих данных
    await manager.update(data={})


# Обновленный getter для получения программы передач и статуса избранного
async def get_tv_program_with_favorite_status(dialog_manager: DialogManager, event_from_user, session, channel_name: str, **kwargs):
    await add_new_user_if_not_exists(session, user_id=str(event_from_user.id), username=event_from_user.username)
    user_id = str(event_from_user.id)

    # Получаем список избранных каналов для пользователя
    favorites = await orm_get_favorites(session, user_id)

    # Проверяем, находится ли текущий канал в списке избранных
    is_in_favorites = any(fav.channel_name == channel_name for fav in favorites)

    # Получаем программу передач для текущего канала
    res = await orm_get_programs(session, channel_name)
    if res:
        res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
    else:
        res = 'Нет программ на оставшуюся часть дня.'

    # Возвращаем данные для отображения
    return {
        'program_title': res,
        'in_favorites': is_in_favorites,  # Статус избранного только для текущего канала
        'not_in_favorites': not is_in_favorites,  # Противоположный статус
    }

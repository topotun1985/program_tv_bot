import logging
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery
from aiogram_dialog import Dialog, Window, DialogManager
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Row, Cancel,ScrollingGroup, Select
from unidecode import unidecode
from config_data.tv_channel_utils import orm_get_favorites
from config_data.channel_states import CHANNEL_STATES


class FavoritesSG(StatesGroup):
    start = State()


# Получаем избранные каналы для пользователя
async def get_favorites(dialog_manager, event_from_user, session, **kwargs):
    user_favorites = await orm_get_favorites(session, event_from_user.id)
    logging.info(f"Избранные каналы: {user_favorites}")

    if user_favorites:
        favorite_channels = [(fav.channel_name, fav.id) for fav in user_favorites]
        # Сохраняем в dialog_data для последующего использования
        dialog_manager.dialog_data['favorite_channels'] = favorite_channels
        return {'favorite_channels': favorite_channels}
    else:
        dialog_manager.dialog_data['favorite_channels'] = []
        return {'favorite_channels': [], 'no_favorites_message': 'У вас нет избранных каналов.'}


# Генерация ID для кнопок
def normalize_widget_id(channel_name):
    return unidecode(channel_name).replace(" ", "_").lower()


async def on_channel_select(callback: CallbackQuery, widget, manager: DialogManager, item_id: str):
    # Получаем данные из dialog_data
    favorite_channels = manager.dialog_data.get('favorite_channels', [])

    # Ищем канал по item_id
    selected_channel = next(
        (fav[0] for fav in favorite_channels if str(fav[1]) == item_id),
        None
    )

    if selected_channel:
        # Переход в состояние, если оно задано
        new_state = CHANNEL_STATES.get(selected_channel)
        if new_state:
            logging.info(f"Переход на канал: {selected_channel} (state: {new_state})")
            await manager.start(new_state, data={'channel_name': selected_channel})
        else:
            logging.warning(f"Состояние для канала {selected_channel} не найдено.")
    else:
        logging.warning(f"Канал с ID {item_id} не найден в избранных.")


# Создание диалога
favorites_dialog = Dialog(
    Window(
        Const('⭐️ <b>Избранные каналы</b> ⭐️\n\n'),

        # Если каналы не найдены
        Const("У вас нет избранных каналов.", when=lambda data, *args, **kwargs: data.get('no_favorites_message') is not None),

        # Прокручиваемая группа кнопок
        ScrollingGroup(
            Select(
                Format('{item[0]}'),  # Печатаем название канала
                id='channel_select',  # ID кнопки
                item_id_getter=lambda x: x[1],  # ID элемента (это ID канала)
                items='favorite_channels',  # Источник данных для элементов
                on_click=on_channel_select,
            ),
            id='favorite_channels_scroll',  # ID для ScrollingGroup
            width=3,  # Ширина кнопок в группе
            height=7  # Ограничение по высоте для прокрутки
        ),
        Row(
            Cancel(Const('◀️ Назад'), id='b_cancel'),
        ),
        getter=get_favorites,  # Передаем геттер
        state=FavoritesSG.start,  # Начальное состояние
    ),
)

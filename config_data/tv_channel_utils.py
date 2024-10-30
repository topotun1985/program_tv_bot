from aiogram_dialog import DialogManager, Dialog, Window
from aiogram_dialog.widgets.text import Const, Format
from aiogram_dialog.widgets.kbd import Cancel
from sqlalchemy.ext.asyncio import AsyncSession
from database.orm_query import orm_get_programs


async def get_tv_program(dialog_manager: DialogManager, event_from_user, session: AsyncSession, channel_name: str, **kwargs):
    res = await orm_get_programs(session, channel_name)
    if res:
        res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
    else:
        res = 'Нет программ на оставшуюся часть дня.'
    return {'program_title': res}


def create_tv_channel_dialog(channel_name: str, state) -> Dialog:
    return Dialog(
        Window(
            Const(f'Программа передач {channel_name} 👇\n'),
            Format('{program_title}'),
            Cancel(Const('◀️ Назад'), id='b_cancel'),
            getter=lambda dialog_manager, event_from_user, session, **kwargs: get_tv_program(
                dialog_manager, event_from_user, session, channel_name
            ),
            state=state
        ),
    )

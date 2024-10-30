from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window
from aiogram_dialog.widgets.kbd import Start, Row
from aiogram_dialog.widgets.text import Const, Format
from handlers.fed_dialog import FedChanSG
from handlers.adult_dialog import AdultSG
from handlers.child_dialog import ChildSG
from handlers.educat_dialog import EduSG
from handlers.entertain_dialog import EntertainSG
from handlers.film_dialog import FilmSG
from handlers.hobbie_dialog import HobbieSG
from handlers.info_dialog import InfoSG
from handlers.music_dialog import MusicSG
from handlers.sport_dialog import SportSG


start_router = Router()


@start_router.message(Command('help'))
async def process_help_command(message: Message):
    await message.answer('What do you want??')


class MainMenuSG(StatesGroup):
    start = State()


async def username_getter(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    return {'username': event_from_user.username or 'Stranger'}


start_dialog = Dialog(
    Window(
        Format('<b>Привет, {username}!</b>\n'),
        Const('Нажми на кнопку,\nчтобы перейти во второй диалог 👇'),
        Row(
            Start(Const('Общероссийские'),id='b_main_menu', state=FedChanSG.start),
            Start(Const('Фильмы и сериалы'), id='b_film', state=FilmSG.start),
        ),
        Row(
            Start(Const('Познавательные'), id='b_educat', state=EduSG.start),
            Start(Const('Спорт'),id='b_sport', state=SportSG.start),
        ),
        Row(
            Start(Const('Детям'), id='b_children', state=ChildSG.start),
            Start(Const('Информация'), id='b_info', state=InfoSG.start),
        ),
        Row(
            Start(Const('Музыка'),id='b_music', state=MusicSG.start),
            Start(Const('Увлечения'), id='b_hobbie', state=HobbieSG.start),
        ),
        Row(
            Start(Const('Развлечения'), id='b_entertain', state=EntertainSG.start),
            Start(Const('18+'), id='b_adult', state=AdultSG.start),
        ),
        Start(Const('Избранные ❤️'), id='go_second', state=FedChanSG.start),
        getter=username_getter,
        state=MainMenuSG.start
    ),
)


@start_router.message(Command('start'))
async def command_start_process(message: Message, dialog_manager: DialogManager):
    await dialog_manager.start(state=MainMenuSG.start, mode=StartMode.RESET_STACK, data={'my_data': '123312'})

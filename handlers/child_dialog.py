from aiogram import Bot, Dispatcher, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Start, Next, Back, Cancel, SwitchTo, ScrollingGroup, Button, Row, Select, Group, Checkbox, ManagedCheckbox
from aiogram_dialog.widgets.text import Const, Format, List, Multi
from database.orm_query import orm_get_programs, orm_get_program
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
from config_data.tv_channel_utils import create_tv_channel_dialog


class ChildSG(StatesGroup):
    start = State()


class StsKidsSG(StatesGroup):
    start = State()


class KinomultSG(StatesGroup):
    start = State()


class UnicumSG(StatesGroup):
    start = State()


class DaVinchi(StatesGroup):
    start = State()


class GulliGirlSG(StatesGroup):
    start = State()


class MyJoySG(StatesGroup):
    start = State()


class MultilandSG(StatesGroup):
    start = State()


class TiJiSG(StatesGroup):
    start = State()


class MultSG(StatesGroup):
    start = State()


class GingerSG(StatesGroup):
    start = State()


class OSG(StatesGroup):
    start = State()


class LoveDoteSG(StatesGroup):
    start = State()


class KidsWorld(StatesGroup):
    start = State()


class SmilikTvSG(StatesGroup):
    start = State()


class SovietMultSG(StatesGroup):
    start = State()


class SkazkiZaikiSG(StatesGroup):
    start = State()


class AniSG(StatesGroup):
    start = State()


class MultimusicSG(StatesGroup):
    start = State()


class LevaTvSG(StatesGroup):
    start = State()


class CartoonClassicsSG(StatesGroup):
    start = State()


child_dialog = Dialog(
    Window(
        Const(text='Детям 👇'),
        ScrollingGroup(
            Start(Const('СТС Kids'), id='b_sts_kids_ch', state=StsKidsSG.start),
            Start(Const('Киномульт'),id='b_kinomult_ch', state=KinomultSG.start),
            Start(Const('Уникум'), id='b_unicum_ch', state=UnicumSG.start),
            Start(Const('Da Vinci'), id='b_davinchi_ch', state=DaVinchi.start),
            Start(Const('Gulli Girl'),id='b_gulli_girl_ch', state=GulliGirlSG.start),
            Start(Const('Радость Моя'), id='b_my_joy_ch', state=MyJoySG.start),
            Start(Const('Мультиландия'), id='b_multiland_ch', state=MultilandSG.start),
            Start(Const('TiJi'),id='b_tiji_ch', state=TiJiSG.start),
            Start(Const('Мульт'), id='b_mult_ch', state=MultSG.start),
            Start(Const('Рыжий'), id='b_ginger_ch', state=GingerSG.start),
            Start(Const('О!'),id='b_o_ch', state=OSG.start),
            Start(Const('Любимое.ТВ'), id='b_love_dote_tv_ch', state=LoveDoteSG.start),
            Start(Const('Детский мир'), id='b_kids_world_ch', state=KidsWorld.start),
            Start(Const('Смайлик ТВ'),id='b_smailik_tv_ch', state=SmilikTvSG.start),
            Start(Const('Советские мультфильмы'), id='b_soviet_mult_ch', state=SovietMultSG.start),
            Start(Const('Сказки Зайки'), id='b_skazki_zaiki_ch', state=SkazkiZaikiSG.start),
            Start(Const('Ani'), id='b_ani_ch', state=AniSG.start),
            Start(Const('Мультимузыка'), id='b_multimusic_ch', state=MultimusicSG.start),
            Start(Const('Лёва'),id='b_leva_tv_ch', state=LevaTvSG.start),
            Start(Const('Cartoon Classics'), id='b_cartoon_classics_ch', state=CartoonClassicsSG.start),
            id='channel_group_3',
            width=3,
            height=5
        ),
        Cancel(Const('◀️ Назад'), id='b_cancel'),
        #getter=username_getter,
        state=ChildSG.start
    ),
)


sts_kids_channel = create_tv_channel_dialog('СТС Kids', StsKidsSG.start)
kinomult_channel = create_tv_channel_dialog('Киномульт', KinomultSG.start)
unicum_channel = create_tv_channel_dialog('Уникум', UnicumSG.start)
davinchi_channel = create_tv_channel_dialog('Da Vinci', DaVinchi.start)
gulli_girl_channel = create_tv_channel_dialog('Gulli Girl', GulliGirlSG.start)
my_joy_channel = create_tv_channel_dialog('Радость Моя', MyJoySG.start)
multiland_channel = create_tv_channel_dialog('Мультиландия', MultilandSG.start)
tiji_channel = create_tv_channel_dialog('TiJi', TiJiSG.start)
mult_channel = create_tv_channel_dialog('Мульт', MultSG.start)
ginger_channel = create_tv_channel_dialog('Рыжий', GingerSG.start)
o_channel = create_tv_channel_dialog('О!', OSG.start)
love_dote_tv_channel = create_tv_channel_dialog('Любимое.ТВ', LoveDoteSG.start)
kids_world_channel = create_tv_channel_dialog('Детский мир', KidsWorld.start)
smilik_tv_channel = create_tv_channel_dialog('Смайлик ТВ', SmilikTvSG.start)
soviet_mult_channel = create_tv_channel_dialog('Советские мультфильмы', SovietMultSG.start)
skazki_zaiki_channel = create_tv_channel_dialog('Сказки Зайки', SkazkiZaikiSG.start)
ani_channel = create_tv_channel_dialog('Ani', AniSG.start)
multimusic_channel = create_tv_channel_dialog('Мультимузыка', MultimusicSG.start)
leva_tv_channel = create_tv_channel_dialog('Лева ТВ', LevaTvSG.start)
cartoon_classics_channel = create_tv_channel_dialog('Cartoon Classics', CartoonClassicsSG.start)

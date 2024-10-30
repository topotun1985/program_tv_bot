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


class EntertainSG(StatesGroup):
    start = State()


class ManSG(StatesGroup):
    start = State()


class LuxurySG(StatesGroup):
    start = State()


class TheatreSG(StatesGroup):
    start = State()


class SarafanSG(StatesGroup):
    start = State()


class O2TvSG(StatesGroup):
    start = State()


class TntFourSG(StatesGroup):
    start = State()


class STSLoveSG(StatesGroup):
    start = State()


class ETvSG(StatesGroup):
    start = State()


class DoteTvSG(StatesGroup):
    start = State()


class KvnTvSG(StatesGroup):
    start = State()


class AnecdotTvSG(StatesGroup):
    start  =State()


class HitTvSG(StatesGroup):
    start = State()


class TwoXTwoSG(StatesGroup):
    start = State()


class SevenTvSG(StatesGroup):
    start = State()


class SaturdaySG(StatesGroup):
    start = State()


entertain_dialog = Dialog(
    Window(
        Const(text='Развлечения 👇'),
        Row(
            Start(Const('Мужской'), id='b_man_ch', state=ManSG.start),
            Start(Const('LUXURY'),id='b_luxury_ch', state=LuxurySG.start),
            Start(Const('Театр'), id='b_theatre_ch', state=TheatreSG.start),
        ),
        Row(
            Start(Const('Сарафан'), id='b_sarafan_ch', state=SarafanSG.start),
            Start(Const('О2ТВ'),id='b_02tv_ch', state=O2TvSG.start),
            Start(Const('ТНТ4'), id='b_tnt_four_ch', state=TntFourSG.start),
        ),
        Row(
            Start(Const('СТС Love'), id='b_sts_love_ch', state=STSLoveSG.start),
            Start(Const('E TV'),id='b_tv5_e_tv_ch', state=ETvSG.start),
            Start(Const('Точка ТВ'), id='b_dote_tv_ch', state=DoteTvSG.start),
        ),
        Row(
            Start(Const('КВН ТВ'), id='b_kvn_tv_ch', state=KvnTvSG.start),
            Start(Const('Анекдот ТВ'),id='b_anecdote_tv_ch', state=AnecdotTvSG.start),
            Start(Const('HITV'), id='b_hitv_ch', state=HitTvSG.start),
        ),
        Row(
            Start(Const('2x2'), id='b_tnt_hd_ch', state=TwoXTwoSG.start),
            Start(Const('7 TV'),id='b_7tv_ch', state=SevenTvSG.start),
            Start(Const('Суббота!'), id='b_saturday_ch', state=SaturdaySG.start),
        ),
        Cancel(Const('◀️ Назад'), id='b_cancel'),
        #getter=username_getter,
        state=EntertainSG.start
    ),
)

man_channel = create_tv_channel_dialog('Мужской', ManSG.start)
luxury_channel = create_tv_channel_dialog('LUXURY', LuxurySG.start)
theatre_channel = create_tv_channel_dialog('Театр', TheatreSG.start)
sarafan_channel = create_tv_channel_dialog('Сарафан', SarafanSG.start)
otwo_tv_channel = create_tv_channel_dialog('О2ТВ', O2TvSG.start)
tnt_four_channel = create_tv_channel_dialog('ТНТ4', TntFourSG.start)
sts_love_channel = create_tv_channel_dialog('СТС Love', STSLoveSG.start)
etv_channel = create_tv_channel_dialog('E TV', ETvSG.start)
dote_tv_channel = create_tv_channel_dialog('Точка ТВ', DoteTvSG.start)
kvn_tv_channel = create_tv_channel_dialog('КВН ТВ', KvnTvSG.start)
anecdot_tv_channel = create_tv_channel_dialog('Анекдот ТВ', AnecdotTvSG.start)
hit_tv_channel = create_tv_channel_dialog('HITV', HitTvSG.start)
two_x_two_channel = create_tv_channel_dialog('2x2', TwoXTwoSG.start)
seven_tv_channel = create_tv_channel_dialog('7 TV', SevenTvSG.start)
saturday_channel = create_tv_channel_dialog('Суббота!', SaturdaySG.start)

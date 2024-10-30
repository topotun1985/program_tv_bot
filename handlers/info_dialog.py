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



class InfoSG(StatesGroup):
    start = State()


class RtviSG(StatesGroup):
    start = State()


class IzvestiyaSG(StatesGroup):
    start = State()


class BloombergSG(StatesGroup):
    start = State()


class AlJaZeeraSG(StatesGroup):
    start = State()


class RussiaTodaySG(StatesGroup):
    start = State()


class DeutscheWelleSG(StatesGroup):
    start = State()


class EuronewsSG(StatesGroup):
    start = State()


class NhkWorldSG(StatesGroup):
    start = State()


class RbkSG(StatesGroup):
    start = State()


class BbcSG(StatesGroup):
    start = State()


class CnbcSG(StatesGroup):
    start = State()


class France24SG(StatesGroup):
    start = State()


class CnnSG(StatesGroup):
    start = State()


class Mir24SG(StatesGroup):
    start = State()


class News360SG(StatesGroup):
    start = State()


info_dialog = Dialog(
    Window(
        Const(text='Информация 👇'),
        Row(
            Start(Const('RTVi'), id='b_rtvi_ch', state=RtviSG),
            Start(Const('Известия'),id='b_izvestiya_ch', state=IzvestiyaSG.start),
            Start(Const('Bloomberg'), id='b_bloomberg_ch', state=BloombergSG.start),
        ),
        Row(
            Start(Const('Al JaZeera'), id='b_al_jazeera_ch', state=AlJaZeeraSG.start),
            Start(Const('Russia Today'),id='b_russia_today_ch', state=RussiaTodaySG.start),
            Start(Const('Deutsche Welle'), id='b_deutsche_welle_ch', state=DeutscheWelleSG.start),
        ),
        Row(
            Start(Const('Евроновости'), id='b_euronews_ch', state=EuronewsSG.start),
            Start(Const('NHK WORLD'),id='b_nhk_world_ch', state=NhkWorldSG.start),
            Start(Const('РБК'), id='b_rbk_ch', state=RbkSG.start),
        ),
        Row(
            Start(Const('BBC'), id='b_bbc_ch', state=BbcSG.start),
            Start(Const('CNBC'),id='b_cnbc_ch', state=CnbcSG.start),
            Start(Const('France 24'), id='b_france24_ch', state=France24SG.start),
        ),
        Row(
            Start(Const('CNN'), id='b_cnn_ch', state=CnnSG.start),
            Start(Const('МИР 24'), id='b_mir24_ch', state=Mir24SG.start),
            Start(Const('360 Новости'),id='b_360news_ch', state=News360SG.start),
        ),

        Cancel(Const('◀️ Назад'), id='b_cancel'),
        #getter=username_getter,
        state=InfoSG.start
    ),
)

rtvi_channel = create_tv_channel_dialog('RTVi', RtviSG.start)
izvestiya_channel = create_tv_channel_dialog('Известия', IzvestiyaSG.start)
bloomberg_channel = create_tv_channel_dialog('Bloomberg', BloombergSG.start)
aljazeera_channel = create_tv_channel_dialog('Al JaZeera', AlJaZeeraSG.start)
russia_today_channel = create_tv_channel_dialog('Russia Today', RussiaTodaySG.start)
deutsche_welle_channel = create_tv_channel_dialog('Deutsche Welle', DeutscheWelleSG.start)
euronews_channel = create_tv_channel_dialog('Евроновости', EuronewsSG.start)
nhk_world_channel = create_tv_channel_dialog('NHK WORLD', NhkWorldSG.start)
rbk_channel = create_tv_channel_dialog('РБК', RbkSG.start)
bbc_channel = create_tv_channel_dialog('BBC', BbcSG.start)
cnbc_channel = create_tv_channel_dialog('CNBC', CnbcSG.start)
france24_channel = create_tv_channel_dialog('France 24', France24SG.start)
cnn_channel = create_tv_channel_dialog('CNN', CnnSG.start)
mir24_channel = create_tv_channel_dialog('МИР 24', Mir24SG.start)
news360_channel = create_tv_channel_dialog('360° Новости', News360SG.start)

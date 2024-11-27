from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Cancel, Row
from aiogram_dialog.widgets.text import Const
from config_data.tv_channel_utils import create_tv_channel_dialog


class AdultSG(StatesGroup):
    start = State()


class CandyTvSG(StatesGroup):
    start = State()


class RussianNightSG(StatesGroup):
    start = State()


class HustlerHdSG(StatesGroup):
    start = State()


class NaughtySG(StatesGroup):
    start = State()


class PlayBoyTvSG(StatesGroup):
    start = State()


class BlueHustler24SG(StatesGroup):
    start = State()


class PenthouseSG(StatesGroup):
    start = State()


class  ExxxoticaSG(StatesGroup):
    start = State()


class RedlightSG(StatesGroup):
    start = State()


class DorcelTSG(StatesGroup):
    start = State()


class BlueHustlerSG(StatesGroup):
    start = State()


class PrivateSpiceSG(StatesGroup):
    start = State()


class EroxSG(StatesGroup):
    start = State()


class BarelyLegalSG(StatesGroup):
    start = State()


class BabesTvSG(StatesGroup):
    start = State()


adult_dialog = Dialog(
    Window(
        Const(text='🔞 <b>Каналы для взрослых</b>'),
        Row(
            Start(Const('Candy TV'), id='b_candy_tv_ch', state=CandyTvSG.start),
            Start(Const('Русская ночь'),id='b_russian_night_ch', state=RussianNightSG.start),
            Start(Const('Hustler HD'), id='b_hustler_hd_ch', state=HustlerHdSG.start),
        ),
        Row(
            Start(Const('Шалун'), id='b_shalun_ch', state=NaughtySG.start),
            Start(Const('PlayBoy TV'),id='b_playboy_tv_ch', state=PlayBoyTvSG.start),
            Start(Const('Blue Hustler 24'), id='b_blue_hustler24_ch', state=BlueHustler24SG.start),
        ),
        Row(
            Start(Const('Penthouse'), id='b_penthouse_ch', state=PenthouseSG.start),
            Start(Const('Exxxotica'),id='b_exxxotica_ch', state=ExxxoticaSG.start),
            Start(Const('Redlight'), id='b_redlight_ch', state=RedlightSG.start),
        ),
        Row(
            Start(Const('Dorcel TV'), id='b_dorcel_tv__ch', state=DorcelTSG.start),
            Start(Const('Blue Hustler'),id='b_blue_hustler_ch', state=BlueHustlerSG.start),
            Start(Const('Private Spice'), id='b_prvate_spice_ch', state=PrivateSpiceSG.start),
        ),
        Row(
            Start(Const('Erox'), id='b_erox_ch', state=EroxSG.start),
            Start(Const('Barely legal'),id='b_barely_legal_ch', state=BarelyLegalSG.start),
            Start(Const('Babes TV'), id='b_babes_tv_ch', state=BabesTvSG.start),
        ),
        Cancel(Const('◀️ Назад'), id='b_cancel'),
        #getter=username_getter,
        state=AdultSG.start
    ),
)


candy_tv_channel = create_tv_channel_dialog('Candy TV', CandyTvSG.start)
russian_night_channel = create_tv_channel_dialog('Русская ночь', RussianNightSG.start)
hustler_hd_channel = create_tv_channel_dialog('Hustler HD', HustlerHdSG.start)
naughty_channel = create_tv_channel_dialog('Шалун', NaughtySG.start)
playboy_tv_channel = create_tv_channel_dialog('Playboy TV', PlayBoyTvSG.start)
blue_hustler_24_channel = create_tv_channel_dialog('Blue Hustler 24', BlueHustler24SG.start)
penthouse_channel = create_tv_channel_dialog('Penthouse', PenthouseSG.start)
exxxotica_channel = create_tv_channel_dialog('Exxxotica', ExxxoticaSG.start)
redlight_channel = create_tv_channel_dialog('Redlight', RedlightSG.start)
dorcel_tv_channel = create_tv_channel_dialog('Dorcel TV', DorcelTSG.start)
blue_hustler_channel = create_tv_channel_dialog('Blue Hustler', BlueHustlerSG.start)
private_spice_channel = create_tv_channel_dialog('Private Spice', PrivateSpiceSG.start)
erox_channel = create_tv_channel_dialog('Erox', EroxSG.start)
barely_legal_channel = create_tv_channel_dialog('Barely legal', BarelyLegalSG.start)
babes_tv_channel = create_tv_channel_dialog('Babes TV', BabesTvSG.start)

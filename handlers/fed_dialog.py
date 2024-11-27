from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Cancel, Row
from aiogram_dialog.widgets.text import Const
from config_data.tv_channel_utils import create_tv_channel_dialog


class FedChanSG(StatesGroup):
    start = State()


class FirstChannel(StatesGroup):
    start = State()


class RussiaOneChannel(StatesGroup):
    start = State()


class MatchTvChannel(StatesGroup):
    start = State()


class NtvChannel(StatesGroup):
    start = State()


class FiveTvChannel(StatesGroup):
    start = State()


class TvCenterChannel(StatesGroup):
    start = State()


class CultureChannel(StatesGroup):
    start = State()


class StsChannel(StatesGroup):
    start = State()


class RenTvChannel(StatesGroup):
    start = State()


class OtpChannel(StatesGroup):
    start = State()


class TntChannel(StatesGroup):
    start = State()


class HomeChannel(StatesGroup):
    start = State()


class FridayChannel(StatesGroup):
    start = State()


class Tv3Channel(StatesGroup):
    start = State()


class MuzTvChannel(StatesGroup):
    start = State()


class CarouselChannel(StatesGroup):
    start = State()


class StarChannel(StatesGroup):
    start = State()


class CheChannel(StatesGroup):
    start = State()


class MirChannel(StatesGroup):
    start = State()


class SpasChannel(StatesGroup):
    start = State()


class YouChannel(StatesGroup):
    start = State()


class Russia24Channel(StatesGroup):
    start = State()


fed_dialog = Dialog(
    Window(
        #Format('<b>Привет, {username}!</b>\n'),
        Const('🇷🇺 <b>Общероссийские каналы</b>'),
        Row(
            Start(Const('Первый'),id='b_first_ch', state=FirstChannel.start),
            #Button(Const('Первый'),id='b_first_ch', on_click='first_channel'),
            Start(Const('Россия 1'), id='b_rus1_ch', state=RussiaOneChannel.start),
            Start(Const('Матч'), id='b_match_ch', state=MatchTvChannel.start),
        ),
        Row(
            Start(Const('НТВ'),id='b_ntv_ch', state=NtvChannel.start),
            Start(Const('Пятый'), id='b_five_ch', state=FiveTvChannel.start),
            Start(Const('Культура'), id='b_culture_ch', state=CultureChannel.start),
        ),
        Row(
            Start(Const('Карусель'),id='b_carousel_ch', state=CarouselChannel.start),
            Start(Const('ОТР'), id='b_otr_ch', state=OtpChannel.start),
            Start(Const('ТВ Центр'), id='b_center_ch', state=TvCenterChannel.start),
        ),
        Row(
            Start(Const('РЕН ТВ'),id='b_rentv_ch', state=RenTvChannel.start),
            Start(Const('Спас ТВ'), id='b_spastv_ch', state=SpasChannel.start),
            Start(Const('СТС'), id='b_sts_ch', state=StsChannel.start),
        ),
        Row(
            Start(Const('Домашний'),id='b_housetv_ch', state=HomeChannel.start),
            Start(Const('ТВ-3'), id='b_tv3_ch', state=Tv3Channel.start),
            Start(Const('Пятница'), id='b_fridaytv_ch', state=FridayChannel.start),
        ),
        Row(
            Start(Const('Звезда'),id='b_starttv_ch', state=StarChannel.start),
            Start(Const('МИР'), id='b_mirtv_ch', state=MirChannel.start),
            Start(Const('ТНТ'), id='b_tnt_ch', state=TntChannel.start),
        ),
        Row(
            Start(Const('МУЗ-ТВ'),id='b_muztv_ch', state=MuzTvChannel.start),
            Start(Const('Че'), id='b_che_ch', state=CheChannel.start),
        ),
        Row(
            Start(Const('Ю'), id='b_you_ch', state=YouChannel.start),
            Start(Const('Россия 24'), id='b_russia24_ch', state=Russia24Channel.start)
        ),
        Cancel(Const('◀️ Назад'), id='b_cancel'),
        #getter=username_getter,
        state=FedChanSG.start
    ),
)


first_channel = create_tv_channel_dialog('Первый канал', FirstChannel.start)
russia_one_channel = create_tv_channel_dialog('Россия 1', RussiaOneChannel.start)
match_tv_channel = create_tv_channel_dialog('Матч', MatchTvChannel.start)
ntv_channel = create_tv_channel_dialog('НТВ', NtvChannel.start)
five_tv_channel = create_tv_channel_dialog('Пятый', FiveTvChannel.start)
tv_center_channel = create_tv_channel_dialog('ТВ Центр', TvCenterChannel.start)
culture_channel = create_tv_channel_dialog('Культура', CultureChannel.start)
sts_channel = create_tv_channel_dialog('СТС', StsChannel.start)
ren_tv_channel = create_tv_channel_dialog('РЕН ТВ', RenTvChannel.start)
otp_channel = create_tv_channel_dialog('ОТР', OtpChannel.start)
tnt_channel = create_tv_channel_dialog('ТНТ', TntChannel.start)
home_channel = create_tv_channel_dialog('Домашний', HomeChannel.start)
friday_channel = create_tv_channel_dialog('Пятница', FridayChannel.start)
tv3_channel = create_tv_channel_dialog('ТВ-3', Tv3Channel.start)
muz_tv_channel = create_tv_channel_dialog('МУЗ ТВ', MuzTvChannel.start)
carousel_channel = create_tv_channel_dialog('Карусель', CarouselChannel.start)
star_channel = create_tv_channel_dialog('Звезда', StarChannel.start)
che_channel = create_tv_channel_dialog('Че', CheChannel.start)
mir_channel = create_tv_channel_dialog('МИР', MirChannel.start)
spas_channel = create_tv_channel_dialog('Спас ТВ', SpasChannel.start)
you_channel = create_tv_channel_dialog('Ю', YouChannel.start)
russia24_channel = create_tv_channel_dialog('Россия 24', Russia24Channel.start)

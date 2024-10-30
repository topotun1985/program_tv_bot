from aiogram import Router, F
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import User
from aiogram_dialog import Dialog, DialogManager, Window
from aiogram_dialog.widgets.kbd import Start, Cancel, Row
from aiogram_dialog.widgets.text import Const, Format
from database.orm_query import orm_get_programs
from sqlalchemy.ext.asyncio import AsyncSession
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
        Const('Общероссийские каналы 👇'),
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
            Start(Const('Ю'), id='b_you_ch', state=YouChannel.start),
        ),
        Row(
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

# async def program_first_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Первый канал'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# first_channel = Dialog(
#     Window(
#         Const(text='Программа передач Первого канала 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_first_channel,
#         state=FirstChannel.start
#     ),
# )

########################################################################

# async def program_russia_one_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Россия 1'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# russia_one_channel = Dialog(
#     Window(
#         Const(text='Программа передач канала Россия 1 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_russia_one_channel,
#         state=RussiaOneChannel.start
#     ),
# )

#########################################################################

# async def program_match_tv_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Матч'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# match_tv_channel = Dialog(
#     Window(
#         Const(text='Программа передач канала Матч ТВ 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_match_tv_channel,
#         state=MatchTvChannel.start
#     ),
# )

#######################################################################################################

# async def program_ntv_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'НТВ'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# ntv_channel = Dialog(
#     Window(
#         Const(text='Программа передач канала НТВ 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_ntv_channel,
#         state=NtvChannel.start
#     ),
# )

######################################################################################################

# async def program_five_tv_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Пятый'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# five_tv_channel = Dialog(
#     Window(
#         Const(text='Программа передач канала Пятый 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_five_tv_channel,
#         state=FiveTvChannel.start
#     ),
# )

####################################################################################################

# async def program_tv_center_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'ТВ Центр'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# tv_center_channel = Dialog(
#     Window(
#         Const(text='Программа передач канала ТВ Центр 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_tv_center_channel,
#         state=TvCenterChannel.start
#     ),
# )

####################################################################################################

# async def program_culture_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Культура'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# culture_channel = Dialog(
#     Window(
#         Const(text='Программа передач канала Культура 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_culture_channel,
#         state=CultureChannel.start
#     ),
# )

#####################################################################################################

# async def program_sts_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'СТС'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# sts_channel = Dialog(
#     Window(
#         Const(text='Программа передач канала СТС 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_sts_channel,
#         state=StsChannel.start
#     ),
# )

#######################################################################################################

# async def program_ren_tv_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'РЕН ТВ'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# ren_tv_channel = Dialog(
#     Window(
#         Const(text='Программа передач канала РЕН ТВ 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_ren_tv_channel,
#         state=RenTvChannel.start
#     ),
# )

######################################################################################################

# async def program_otp_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'ОТР'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# otp_channel = Dialog(
#     Window(
#         Const(text='Программа передач канала ОТР 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_otp_channel,
#         state=OtpChannel.start
#     ),
# )

#####################################################################################################

# async def program_tnt_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'ТНТ'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# tnt_channel = Dialog(
#     Window(
#         Const(text='Программа передач канала ТНТ 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_tnt_channel,
#         state=TntChannel.start
#     ),
# )

######################################################################################################

# async def program_home_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Домашний'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# home_channel = Dialog(    Window(
#         Const(text='Программа передач канала Домашний 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_home_channel,
#         state=HomeChannel.start
#     ),
# )

######################################################################################################

# async def program_friday_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Пятница'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# friday_channel = Dialog(    Window(
#         Const(text='Программа передач канала Пятница 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_friday_channel,
#         state=FridayChannel.start
#     ),
# )

#######################################################################################################

# async def program_tv3_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'ТВ-3'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# tv3_channel = Dialog(    Window(
#         Const(text='Программа передач канала ТВ-3 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_tv3_channel,
#         state=Tv3Channel.start
#     ),
# )

#####################################################################################################

# async def program_muz_tv_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'МУЗ ТВ'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# muz_tv_channel = Dialog(    Window(
#         Const(text='Программа передач канала МУЗ ТВ 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_muz_tv_channel,
#         state=MuzTvChannel.start
#     ),
# )

######################################################################################################

# async def program_carousel_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Карусель'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# carousel_channel = Dialog(    Window(
#         Const(text='Программа передач канала Карусель 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_carousel_channel,
#         state=CarouselChannel.start
#     ),
# )

#####################################################################################################

# async def program_star_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Звезда'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# star_channel = Dialog(    Window(
#         Const(text='Программа передач канала Звезда 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_star_channel,
#         state=StarChannel.start
#     ),
# )

#####################################################################################################

# async def program_che_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Че'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# che_channel = Dialog(    Window(
#         Const(text='Программа передач канала Че 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_che_channel,
#         state=CheChannel.start
#     ),
# )

##################################################################################################

# async def program_mir_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'МИР'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# mir_channel = Dialog(    Window(
#         Const(text='Программа передач канала МИР 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_mir_channel,
#         state=MirChannel.start
#     ),
# )

####################################################################################################

# async def program_spas_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Спас ТВ'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# spas_channel = Dialog(    Window(
#         Const(text='Программа передач канала Спас ТВ 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_spas_channel,
#         state=SpasChannel.start
#     ),
# )

#####################################################################################################

# async def program_you_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Ю'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# you_channel = Dialog(    Window(
#         Const(text='Программа передач канала Ю 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_you_channel,
#         state=YouChannel.start
#     ),
# )

##################################################################################################

# async def program_russia24_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Россия 24'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M') } - {program.program_title}" for program in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'

#     return {'program_title': res}


# russia24_channel = Dialog(    Window(
#         Const(text='Программа передач канала Россия 24 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_russia24_channel,
#         state=Russia24Channel.start
#     ),
# )

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
from config_data.tv_channel_utils import create_tv_channel_dialog
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime


class FilmSG(StatesGroup):
    start = State()


class KinoTvSG(StatesGroup):
    start = State()


class A2SG(StatesGroup):
    start = State()


class BlackSG(StatesGroup):
    start = State()


class SciFiSG(StatesGroup):
    start = State()


class HollywoodSG(StatesGroup):
    start = State()


class VijuTv1000SG(StatesGroup):
    start = State()


class VijuTv1000RussianSG(StatesGroup):
    start = State()


class Tv21SG(StatesGroup):
    start = State()


class DomKinoSG(StatesGroup):
    start = State()


class IlluzionSG(StatesGroup):
    start = State()


class IndianKinoSG(StatesGroup):
    start = State()


class KinodateSG(StatesGroup):
    start = State()


class KinoHit(StatesGroup):
    start = State()


class NstSG(StatesGroup):
    start = State()


class NativeKinoSG(StatesGroup):
    start = State()


class OurNewKinoSG(StatesGroup):
    start = State()


class RusIlluzionSG(StatesGroup):
    start = State()


class KinopremierSG(StatesGroup):
    start = State()


class FenixKinoSG(StatesGroup):
    start = State()


class EurokinoSG(StatesGroup):
    start = State()


class IndiaSG(StatesGroup):
    start = State()


class MirSerialSG(StatesGroup):
    start = State()


class VijuTv1000ActionSG(StatesGroup):
    start = State()


class RedSG(StatesGroup):
    start = State()


class KinoseriaSG(StatesGroup):
    start = State()


class KinocomedySG(StatesGroup):
    start = State()


class RusRomanSG(StatesGroup):
    start = State()


class RusBestsellerSG(StatesGroup):
    start = State()


class A1SG(StatesGroup):
    start = State()


class RusDetectiveSG(StatesGroup):
    start = State()


class MenKinoSG(StatesGroup):
    start = State()


class ComedySG(StatesGroup):
    start = State()


class VijuPlusComedySG(StatesGroup):
    start = State()


class VijuPlusMegahitSG(StatesGroup):
    start = State()


class VijuPlusPremiereSG(StatesGroup):
    start = State()


class FoxHdSG(StatesGroup):
    start = State()


class HollywoodHDSG(StatesGroup):
    start = State()


class ShockTvHDSG(StatesGroup):
    start = State()


class ComedyHDSG(StatesGroup):
    start = State()


class AmediaPremiumHDSG(StatesGroup):
    start = State()


class ScaryHDSG(StatesGroup):
    start = State()


class BollywoodHDSG(StatesGroup):
    start = State()


class PremiumHDSG(StatesGroup):
    start = State()


class SpicyHDSG(StatesGroup):
    start = State()


class CinemaSG(StatesGroup):
    start = State()


class DomKinoPremiumHDSG(StatesGroup):
    start = State()


class OurTvSG(StatesGroup):
    start = State()


class SoulTvSG(StatesGroup):
    start = State()


class NtvSerialSG(StatesGroup):
    start = State()


class FilmBoxArthouseSG(StatesGroup):
    start = State()


class AmediaHitSG(StatesGroup):
    start = State()


class SovietKinoSG(StatesGroup):
    start = State()


class OKinoSG(StatesGroup):
    start = State()


class VijuSerialSG(StatesGroup):
    start = State()


class MosfilmGoldSG(StatesGroup):
    start = State()


class KinoJam1SG(StatesGroup):
    start = State()


class KinoJam2SG(StatesGroup):
    start = State()


class StartAirSG(StatesGroup):
    start = State()


class StartWorldSG(StatesGroup):
    start = State()


class NtvHitSG(StatesGroup):
    start = State()


class SapfirSG(StatesGroup):
    start = State()


class DayWinSG(StatesGroup):
    start = State()


class TimelessDiziSG(StatesGroup):
    start = State()


class KinomanSG(StatesGroup):
    start = State()


class KinomixSG(StatesGroup):
    start = State()


class ScreamSG(StatesGroup):
    start = State()


class CriminalSG(StatesGroup):
    start = State()


class LovestorySG(StatesGroup):
    start = State()


class FavoriteSG(StatesGroup):
    start = State()


class FavoriteKinoSG(StatesGroup):
    start = State()


class KinoScarySG(StatesGroup):
    start = State()


class Tehno24SG(StatesGroup):
    start = State()


film_dialog = Dialog(
    Window(
        #Format('<b>Привет, {username}!</b>\n'),
        Const('Фильмы и сериалы 👇'),
        ScrollingGroup(
            Start(Const('Кино ТВ'),id='b_kinotv_ch', state=KinoTvSG.start),
            Start(Const('А2'), id='b_a2_ch', state=A2SG.start),
            Start(Const('.black'), id='b_black_ch', state=BlackSG.start),
            Start(Const('.sci-fi'),id='b_sci_ch', state=SciFiSG.start),
            Start(Const('Hollywood'), id='b_hollywood_ch', state=HollywoodSG.start),
            Start(Const('viju TV1000'), id='b_viju1000_ch', state=VijuTv1000SG.start),
            Start(Const('viju TV1000 русское'),id='b_viju1000rus_ch', state=VijuTv1000RussianSG.start),
            Start(Const('TV XXI'), id='b_tv21_ch', state=Tv21SG.start),
            Start(Const('Дом Кино'), id='b_domkino_ch', state=DomKinoSG.start),
            Start(Const('Иллюзион +'),id='b_illuzion_ch', state=IlluzionSG.start),
            Start(Const('Индийское кино'), id='b_indian_ch', state=IndianKinoSG.start),
            Start(Const('Киносвидание'), id='b_kinodate_ch', state=KinodateSG.start),
            Start(Const('Кинохит'),id='b_kinohit_ch', state=KinoHit.start),
            Start(Const('НСТ'), id='b_nst_ch', state=NstSG.start),
            Start(Const('Родное кино'), id='b_native_kino_ch', state=NativeKinoSG.start),
            Start(Const('Наше новое кино'),id='b_our_new_kino_ch', state=OurNewKinoSG.start),
            Start(Const('Русский Иллюзион'), id='b_rus_illuzion_ch', state=RusIlluzionSG.start),
            Start(Const('Кинопремьера'), id='b_kinopremier_ch', state=KinopremierSG.start),
            Start(Const('Феникс+Кино'),id='b_fenix_kino_ch', state=FenixKinoSG.start),
            Start(Const('Еврокино'),id='b_eurokino_ch', state=EurokinoSG.start),
            Start(Const('Индия'), id='b_india_ch', state=IndiaSG.start),
            Start(Const('Мир сериала'), id='b_mir_serial_ch', state=MirSerialSG.start),
            Start(Const('viju TV1000 action'),id='b_viju1000_action_ch', state=VijuTv1000ActionSG.start),
            Start(Const('.red'), id='b_red_ch', state=RedSG.start),
            Start(Const('Киносерия'),id='b_kinoseria_ch', state=KinoseriaSG.start),
            Start(Const('Кинокомедия'), id='b_kinocomedy_ch', state=KinocomedySG.start),
            Start(Const('Русский роман'), id='b_rus_roman_ch', state=RusRomanSG.start),
            Start(Const('Русский бестселлер'),id='b_rus_bestseller_ch', state=RusBestsellerSG.start),
            Start(Const('A1'), id='b_a1_ch', state=A1SG.start),
            Start(Const('Русский Детектив'), id='b_rus_detectiev_ch', state=RusDetectiveSG.start),
            Start(Const('Мужское кино'),id='b_men_kino_ch', state=MenKinoSG.start),
            Start(Const('Комедия'), id='b_comedy_ch', state=ComedySG.start),
            Start(Const('viju+ Comedy'), id='b_viju_comedy_ch', state=VijuPlusComedySG.start),
            Start(Const('viju+ Megahit'),id='b_viju_megahit_ch', state=VijuPlusMegahitSG.start),
            Start(Const('viju+ Premiere'), id='b_viju_premiere_ch', state=VijuPlusPremiereSG.start),
            Start(Const('Fox HD'), id='b_fox_hd_ch', state=FoxHdSG.start),
            Start(Const('Hollywood HD'), id='b_hollywood_ch', state=HollywoodHDSG.start),
            Start(Const('Шокирующее HD'), id='b_shock_tv_ch', state=ShockTvHDSG.start),
            Start(Const('Комедийное HD'),id='b_comedytv_ch', state=ComedyHDSG.start),
            Start(Const('Amedia Premium HD'), id='b_amedia_premium_hd_ch', state=AmediaPremiumHDSG.start),
            Start(Const('Страшное HD'),id='b_scary_hd__ch', state=ScaryHDSG.start),
            Start(Const('Bollywood HD '), id='b_bollywood_hd_ch', state=BollywoodHDSG.start),
            Start(Const('Премиальное HD'), id='b_premium_hd_ch', state=PremiumHDSG.start),
            Start(Const('Остросюжетное HD'),id='b_spicy_hd_ch', state=SpicyHDSG.start),
            Start(Const('Cinema'), id='b_cinema_tv_ch', state=CinemaSG.start),
            Start(Const('Дом Кино Премиум HD'),id='b_dom_kino_premium_hd_ch', state=DomKinoPremiumHDSG.start),
            Start(Const('Наше'), id='b_our_tv_ch', state=OurTvSG.start),
            Start(Const('Душевное'), id='b_soul_tv_ch', state=SoulTvSG.start),
            Start(Const('НТВ Сериал'),id='b_ntv_serial_ch', state=NtvSerialSG.start),
            Start(Const('FilmBox Arthouse'),id='b_filmbox_arthouse_ch', state=FilmBoxArthouseSG.start),
            Start(Const('Amedia Hit'), id='b_amedia_hit_ch', state=AmediaHitSG.start),
            Start(Const('Советское кино'), id='b_soviet_kino_ch', state=SovietKinoSG.start),
            Start(Const('О!Кино'),id='b_o_kino_ch', state=OKinoSG.start),
            Start(Const('viju+ Serial'), id='b_viju_serial_ch', state=VijuSerialSG.start),
            Start(Const('Мосфильм. Золотая коллекция'), id='b_mosfilm_ch', state=MosfilmGoldSG.start),
            Start(Const('KinoJam 1'), id='b_kinojam1_ch', state=KinoJam1SG.start),
            Start(Const('KinoJam 2'), id='b_kinojam2_ch', state=KinoJam2SG.start),
            Start(Const('START Air'), id='b_start_air_ch', state=StartAirSG.start),
            Start(Const('START World'),id='b_start_world_ch', state=StartWorldSG.start),
            Start(Const('НТВ Хит'), id='b_ntv_hit_ch', state=NtvHitSG.start),
            Start(Const('Сапфир'), id='b_sapfir_ch', state=SapfirSG.start),
            Start(Const('День Победы'), id='b_day_win_ch', state=DayWinSG.start),
            Start(Const('Timeless Dizi Channel'), id='b_timeless_dizi_ch', state=TimelessDiziSG.start),
            Start(Const('Киноман'), id='b_kinoman_ch', state=KinomanSG.start),
            Start(Const('Киномикс'),id='b_kinomix_ch', state=KinomixSG.start),
            Start(Const('Scream'), id='b_scream_ch', state=ScreamSG.start),
            Start(Const('Криминальное'),id='b_criminal_ch', state=CriminalSG.start),
            Start(Const('Лавстори'), id='b_lovestory_ch', state=LovestorySG.start),
            Start(Const('Любимое'), id='b_favorite_ch', state=FavoriteSG.start),
            Start(Const('Любимое кино'), id='b_favorite_kino_ch', state=FavoriteKinoSG.start),
            Start(Const('Киноужас'), id='b_favorite_kino_ch', state=KinoScarySG.start),
            Start(Const('Техно 24'), id='b_tehno24_ch', state=Tehno24SG.start),
            id='channels_group_1',
            width=3,
            height=6
        ),
        Cancel(Const('◀️ Назад'), id='b_cancel'),
        #getter=username_getter,
        state=FilmSG.start
    ),
)


kino_tv_channel = create_tv_channel_dialog('Кино ТВ', KinoTvSG.start)
a2_tv_channel = create_tv_channel_dialog('А2', A2SG.start)
black_channel = create_tv_channel_dialog('.black', BlackSG.start)
sci_fi_channel = create_tv_channel_dialog('.sci-fi', SciFiSG.start)
hollywood_channel = create_tv_channel_dialog('Hollywood', HollywoodSG.start)
viju_tv1000_channel = create_tv_channel_dialog('viju TV1000', VijuTv1000SG.start)
viju_tv1000_russian_channel = create_tv_channel_dialog('viju TV1000 русское', VijuTv1000RussianSG.start)
tv21_channel = create_tv_channel_dialog('TV XXI', Tv21SG.start)
dom_kino_channel = create_tv_channel_dialog('Дом Кино', DomKinoSG.start)
illuzion_channel = create_tv_channel_dialog('Иллюзион +', IlluzionSG.start)
indian_kino_channel = create_tv_channel_dialog('Индийское кино', IndianKinoSG.start)
kinodate_channel = create_tv_channel_dialog('Киносвидание', KinodateSG.start)
kinohit_channel = create_tv_channel_dialog('Кинохит', KinoHit.start)
nst_channel = create_tv_channel_dialog('НСТ', NstSG.start)
native_kino_channel = create_tv_channel_dialog('Родное кино', NativeKinoSG.start)
our_new_kino_channel = create_tv_channel_dialog('Наше новое кино', OurNewKinoSG.start)
rus_illuzion_channel = create_tv_channel_dialog('Русский Иллюзион', RusIlluzionSG.start)
kinopremier_channel = create_tv_channel_dialog('Кинопремьера', KinopremierSG.start)
fenix_kino_channel = create_tv_channel_dialog('Феникс+Кино', FenixKinoSG.start)
eurokino_channel = create_tv_channel_dialog('Еврокино', EurokinoSG.start)
india_channel = create_tv_channel_dialog('Индия', IndiaSG.start)
mir_serial_channel = create_tv_channel_dialog('Мир сериала', MirSerialSG.start)
viju_tv1000_action_channel = create_tv_channel_dialog('viju TV1000 action', VijuTv1000ActionSG.start)
red_channel = create_tv_channel_dialog('.red', RedSG.start)
kinoseria_channel = create_tv_channel_dialog('Киносерия', KinoseriaSG.start)
kinocomedy_channel = create_tv_channel_dialog('Кинокомедия', KinocomedySG.start)
rus_roman_channel = create_tv_channel_dialog('Русский роман', RusRomanSG.start)
rus_bestseller_channel = create_tv_channel_dialog('Русский бестселлер', RusBestsellerSG.start)
a1_channel = create_tv_channel_dialog('A1', A1SG.start)
rus_detective_channel = create_tv_channel_dialog('Русский Детектив', RusDetectiveSG.start)
men_kino_channel = create_tv_channel_dialog('Мужское кино', MenKinoSG.start)
comedy_channel = create_tv_channel_dialog('Комедия', ComedySG.start)
viju_plus_comedy_channel = create_tv_channel_dialog('viju+ Comedy', VijuPlusComedySG.start)
viju_plus_megahit_channel = create_tv_channel_dialog('viju+ Megahit', VijuPlusMegahitSG.start)
viju_plus_premiere_channel = create_tv_channel_dialog('viju+ Premiere', VijuPlusPremiereSG.start)
fox_hd_channel = create_tv_channel_dialog('Fox HD', FoxHdSG.start)
hollywood_hd_channel = create_tv_channel_dialog('Hollywood HD', HollywoodHDSG.start)
shock_hd_channel = create_tv_channel_dialog('Шокирующее HD', ShockTvHDSG.start)
comedy_hd_channel = create_tv_channel_dialog('Комедийное HD', ComedyHDSG.start)
amedia_premium_hd_channel = create_tv_channel_dialog('Amedia Premium HD', AmediaPremiumHDSG.start)
scary_hd_channel = create_tv_channel_dialog('Страшное HD', ScaryHDSG.start)
bollywood_hd_channel = create_tv_channel_dialog('Bollywood HD', BollywoodHDSG.start)
premium_hd_channel = create_tv_channel_dialog('Премиальное HD', PremiumHDSG.start)
spicy_hd_channel = create_tv_channel_dialog('Остросюжетное HD', SpicyHDSG.start)
cinema_channel = create_tv_channel_dialog('Cinema', CinemaSG.start)
dom_kino_pemium_hd_channel = create_tv_channel_dialog('Дом кино Премиум HD', DomKinoPremiumHDSG.start)
our_tv_channel = create_tv_channel_dialog('Наше', OurTvSG.start)
soul_tv_channel = create_tv_channel_dialog('Душевное', SoulTvSG.start)
ntv_serial_channel = create_tv_channel_dialog('НТВ Сериал', NtvSerialSG.start)
filmbox_arthouse_channel = create_tv_channel_dialog('FilmBox Arthouse', FilmBoxArthouseSG.start)
amedia_hit_channel = create_tv_channel_dialog('Amedia Hit', AmediaHitSG.start)
soviet_kino_channel = create_tv_channel_dialog('Советское кино', SovietKinoSG.start)
o_kino_channel = create_tv_channel_dialog('О!Кино', OKinoSG.start)
viju_serial_channel = create_tv_channel_dialog('viju+ Serial', VijuSerialSG.start)
mosfilm_channel = create_tv_channel_dialog('Мосфильм. Золотая коллекция', MosfilmGoldSG.start)
kinojam1_channel = create_tv_channel_dialog('KinoJam 1', KinoJam1SG.start)
kinojam2_channel = create_tv_channel_dialog('KinoJam 2', KinoJam2SG.start)
start_air_channel = create_tv_channel_dialog('Start Air', StartAirSG.start)
start_world_channel = create_tv_channel_dialog('Start World', StartWorldSG.start)
ntv_hit_channel = create_tv_channel_dialog('НТВ Хит', NtvHitSG.start)
sapfir_channel = create_tv_channel_dialog('Сапфир', SapfirSG.start)
day_win_channel = create_tv_channel_dialog('День Победы', DayWinSG.start)
timeless_dizi_channel = create_tv_channel_dialog('Timeless Dizi Channel', TimelessDiziSG.start)
kinoman_channel = create_tv_channel_dialog('Киноман', KinomanSG.start)
kinomix_channel = create_tv_channel_dialog('Киномикс', KinomixSG.start)
scream_channel = create_tv_channel_dialog('Scream', ScreamSG.start)
criminal_channel = create_tv_channel_dialog('Криминальное', CriminalSG.start)
lovestory_channel = create_tv_channel_dialog('Лавстори', LovestorySG.start)
favorite_channel = create_tv_channel_dialog('Любимое', FavoriteSG.start)
favorite_kino_channel = create_tv_channel_dialog('Любимое кино', FavoriteKinoSG.start)
kinoscary_channel = create_tv_channel_dialog('Киноужас', KinoScarySG.start)
tehno24_channel = create_tv_channel_dialog('Техно 24', Tehno24SG.start)


######################################################################################################

# async def program_kino_tv_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Кино ТВ'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kino_tv_channel = Dialog(
#     Window(
#         Const(text='Программа передач Кино ТВ 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kino_tv_channel,
#         state=KinoTvSG.start
#     ),
# )

########################################################################################################

# async def program_a2_tv_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'А2'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# a2_tv_channel = Dialog(
#     Window(
#         Const(text='Программа передач А2 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_a2_tv_channel,
#         state=A2SG.start
#     ),
# )

#########################################################################################################

# async def program_black_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = '.black'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# black_channel = Dialog(
#     Window(
#         Const(text='Программа передач .black 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_black_channel,
#         state=BlackSG.start
#     ),
# )

#########################################################################################################

# async def program_sci_fi_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = '.sci-fi'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# sci_fi_channel = Dialog(
#     Window(
#         Const(text='Программа передач .sci-fi 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_sci_fi_channel,
#         state=SciFiSG.start
#     ),
# )

##########################################################################################################

# async def program_hollywood_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Hollywood'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# hollywood_channel = Dialog(
#     Window(
#         Const(text='Программа передач Hollywood 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_hollywood_channel,
#         state=HollywoodSG.start
#     ),
# )

###########################################################################################################

# async def program_viju_tv1000_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'viju TV1000'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# viju_tv1000_channel = Dialog(
#     Window(
#         Const(text='Программа передач viju TV1000 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_viju_tv1000_channel,
#         state=VijuTv1000SG.start
#     ),
# )

#############################################################################################################

# async def program_viju_tv1000_russian_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'viju TV1000 русское'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# viju_tv1000_russian_channel = Dialog(
#     Window(
#         Const(text='Программа передач viju TV1000 русское 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_viju_tv1000_russian_channel,
#         state=VijuTv1000RussianSG.start
#     ),
# )

#######################################################################################################

# async def program_tv21_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'TV XXI'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# tv21_channel = Dialog(
#     Window(
#         Const(text='Программа передач TV XXI 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_tv21_channel,
#         state=Tv21SG.start
#     ),
# )

#####################################################################################################

# async def program_dom_kino_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Дом Кино'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# dom_kino_channel = Dialog(
#     Window(
#         Const(text='Программа передач Дом Кино 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_dom_kino_channel,
#         state=DomKinoSG.start
#     ),
# )

######################################################################################################

# async def program_illuzion_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Иллюзион +'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# illuzion_channel = Dialog(
#     Window(
#         Const(text='Программа передач Иллюзион + 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_illuzion_channel,
#         state=IlluzionSG.start
#     ),
# )

#########################################################################################################

# async def program_indian_kino_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Индийское кино'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# indian_kino_channel = Dialog(
#     Window(
#         Const(text='Программа передач Индийское кино 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_indian_kino_channel,
#         state=IndianKinoSG.start
#     ),
# )

#####################################################################################################

# async def program_kinodate_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Киносвидание'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kinodate_channel = Dialog(
#     Window(
#         Const(text='Программа передач Киносвидание 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kinodate_channel,
#         state=KinodateSG.start
#     ),
# )

######################################################################################################

# async def program_kinohit_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Кинохит'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kinohit_channel = Dialog(
#     Window(
#         Const(text='Программа передач Кинохит 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kinohit_channel,
#         state=KinoHit.start
#     ),
# )

#######################################################################################################

# async def program_nst_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'НСТ'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# nst_channel = Dialog(
#     Window(
#         Const(text='Программа передач НСТ 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_nst_channel,
#         state=NstSG.start
#     ),
# )

#######################################################################################################

# async def program_native_kino_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Родное кино'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# native_kino_channel = Dialog(
#     Window(
#         Const(text='Программа передач Родное кино 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_native_kino_channel,
#         state=NativeKinoSG.start
#     ),
# )

######################################################################################################

# async def program_our_new_kino_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Наше новое кино'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# our_new_kino_channel = Dialog(
#     Window(
#         Const(text='Программа передач Наше новое кино 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_our_new_kino_channel,
#         state=OurNewKinoSG.start
#     ),
# )

############################################################################################

# async def program_rus_illuzion_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Русский Иллюзион'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# rus_illuzion_channel = Dialog(
#     Window(
#         Const(text='Программа передач Русский Иллюзион 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_rus_illuzion_channel,
#         state=RusIlluzionSG.start
#     ),
# )

#############################################################################################

# async def program_kinopremier_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Кинопремьера'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kinopremier_channel = Dialog(
#     Window(
#         Const(text='Программа передач Кинопремьера 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kinopremier_channel,
#         state=KinopremierSG.start
#     ),
# )

#############################################################################################

# async def program_fenix_kino_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Феникс+Кино'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# fenix_kino_channel = Dialog(
#     Window(
#         Const(text='Программа передач Феникс+Кино 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_fenix_kino_channel,
#         state=FenixKinoSG.start
#     ),
# )

############################################################################################

# async def program_eurokino_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Еврокино'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# eurokino_channel = Dialog(
#     Window(
#         Const(text='Программа передач Еврокино 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_eurokino_channel,
#         state=EurokinoSG.start
#     ),
# )

############################################################################################

# async def program_india_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Индия'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# india_channel = Dialog(
#     Window(
#         Const(text='Программа передач Индия 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_india_channel,
#         state=IndiaSG.start
#     ),
# )

############################################################################################

# async def program_mir_serial_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Мир сериала'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# mir_serial_channel = Dialog(
#     Window(
#         Const(text='Программа передач Мир сериала 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_mir_serial_channel,
#         state=MirSerialSG.start
#     ),
# )

#########################################################################################

# async def program_viju_tv1000_action_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'viju TV1000 action'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# viju_tv1000_action_channel = Dialog(
#     Window(
#         Const(text='Программа передач viju TV1000 action 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_viju_tv1000_action_channel,
#         state=VijuTv1000ActionSG.start
#     ),
# )

#####################################################################################

# async def program_red_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = '.red'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# red_channel = Dialog(
#     Window(
#         Const(text='Программа передач .red 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_red_channel,
#         state=RedSG.start
#     ),
# )

########################################################################################

# async def program_kinoseria_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Киносерия'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kinoseria_channel = Dialog(
#     Window(
#         Const(text='Программа передач Киносерия 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kinoseria_channel,
#         state=KinoseriaSG.start
#     ),
# )

##################################################################################

# async def program_kinocomedy_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Кинокомедия'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kinocomedy_channel = Dialog(
#     Window(
#         Const(text='Программа передач Кинокомедия 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kinocomedy_channel,
#         state=KinocomedySG.start
#     ),
# )

###################################################################################

# async def program_rus_roman_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Русский роман'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# rus_roman_channel = Dialog(
#     Window(
#         Const(text='Программа передач Русский роман 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_rus_roman_channel,
#         state=RusRomanSG.start
#     ),
# )

###############################################################################

# async def program_rus_bestseller_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Русский бестселлер'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# rus_bestseller_channel = Dialog(
#     Window(
#         Const(text='Программа передач Русский бестселлер 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_rus_bestseller_channel,
#         state=RusBestsellerSG.start
#     ),
# )

###########################################################################

# async def program_a1_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'A1'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# a1_channel = Dialog(
#     Window(
#         Const(text='Программа передач A1 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_a1_channel,
#         state=A1SG.start
#     ),
# )

###########################################################################

# async def program_rus_detective_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Русский Детектив'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# rus_detective_channel = Dialog(
#     Window(
#         Const(text='Программа передач Русский Детектив 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_rus_detective_channel,
#         state=RusDetectiveSG.start
#     ),
# )

#########################################################################

# async def program_men_kino_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Мужское кино'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# men_kino_channel = Dialog(
#     Window(
#         Const(text='Программа передач Мужское кино 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_men_kino_channel,
#         state=MenKinoSG.start
#     ),
# )

###########################################################################

# async def program_comedy_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Комедия'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# comedy_channel = Dialog(
#     Window(
#         Const(text='Программа передач Комедия 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_comedy_channel,
#         state=ComedySG.start
#     ),
# )

##########################################################################

# async def program_viju_plus_comedy_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'viju+ Comedy'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# viju_plus_comedy_channel = Dialog(
#     Window(
#         Const(text='Программа передач viju+ Comedy 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_viju_plus_comedy_channel,
#         state=VijuPlusComedySG.start
#     ),
# )

#######################################################################

# async def program_viju_plus_megahit_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'viju+ Megahit'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# viju_plus_megahit_channel = Dialog(
#     Window(
#         Const(text='Программа передач viju+ Megahit 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_viju_plus_megahit_channel,
#         state=VijuPlusMegahitSG.start
#     ),
# )

########################################################################

# async def program_viju_plus_premiere_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'viju+ Premiere'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# viju_plus_premiere_channel = Dialog(
#     Window(
#         Const(text='Программа передач viju+ Premiere 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_viju_plus_premiere_channel,
#         state=VijuPlusPremiereSG.start
#     ),
# )

########################################################################

# async def program_fox_hd_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Fox HD'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# fox_hd_channel = Dialog(
#     Window(
#         Const(text='Программа передач Fox HD 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_fox_hd_channel,
#         state=FoxHdSG.start
#     ),
# )

#######################################################################

# async def program_hollywood_hd_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Hollywood HD'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# hollywood_hd_channel = Dialog(
#     Window(
#         Const(text='Программа передач Hollywood HD 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_hollywood_hd_channel,
#         state=HollywoodHDSG.start
#     ),
# )

#########################################################################

# async def program_shock_hd_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Шокирующее HD'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# shock_hd_channel = Dialog(
#     Window(
#         Const(text='Программа передач Шокирующее HD 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_shock_hd_channel,
#         state=ShockTvHDSG.start
#     ),
# )

#######################################################################

# async def program_comedy_hd_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Комедийное HD'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# comedy_hd_channel = Dialog(
#     Window(
#         Const(text='Программа передач Комедийное HD 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_comedy_hd_channel,
#         state=ComedyHDSG.start
#     ),
# )

########################################################################

# async def program_amedia_premium_hd_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Amedia Premium HD'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# amedia_premium_hd_channel = Dialog(
#     Window(
#         Const(text='Программа передач Amedia Premium HD 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_amedia_premium_hd_channel,
#         state=AmediaPremiumHDSG.start
#     ),
# )

########################################################################

# async def program_scary_hd_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Страшное HD'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# scary_hd_channel = Dialog(
#     Window(
#         Const(text='Программа передач Страшное HD 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_scary_hd_channel,
#         state=ScaryHDSG.start
#     ),
# )

########################################################################

# async def program_bollywood_hd_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Bollywood HD'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# bollywood_hd_channel = Dialog(
#     Window(
#         Const(text='Программа передач Bollywood HD 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_bollywood_hd_channel,
#         state=BollywoodHDSG.start
#     ),
# )

########################################################################

# async def program_premium_hd_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Премиальное HD'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# premium_hd_channel = Dialog(
#     Window(
#         Const(text='Программа передач Премиальное HD 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_premium_hd_channel,
#         state=PremiumHDSG.start
#     ),
# )

######################################################################

# async def program_spicy_hd_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Остросюжетное HD'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# spicy_hd_channel = Dialog(
#     Window(
#         Const(text='Программа передач Остросюжетное HD 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_spicy_hd_channel,
#         state=SpicyHDSG.start
#     ),
# )

########################################################################

# async def program_cinema_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Cinema'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# cinema_channel = Dialog(
#     Window(
#         Const(text='Программа передач Cinema 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_cinema_channel,
#         state=CinemaSG.start
#     ),
# )

##########################################################################

# async def program_dom_kino_pemium_hd_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Дом кино Премиум HD'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# dom_kino_pemium_hd_channel = Dialog(
#     Window(
#         Const(text='Программа передач Дом кино Премиум HD 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_dom_kino_pemium_hd_channel,
#         state=DomKinoPremiumHDSG.start
#     ),
# )

##########################################################################

# async def program_our_tv_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Наше'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# our_tv_channel = Dialog(
#     Window(
#         Const(text='Программа передач Наше 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_our_tv_channel,
#         state=OurTvSG.start
#     ),
# )

####################################################################

# async def program_soul_tv_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Душевное'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# soul_tv_channel = Dialog(
#     Window(
#         Const(text='Программа передач Душевное 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_soul_tv_channel,
#         state=SoulTvSG.start
#     ),
# )

######################################################################

# async def program_ntv_serial_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'НТВ Сериал'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# ntv_serial_channel = Dialog(
#     Window(
#         Const(text='Программа передач НТВ Сериал 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_ntv_serial_channel,
#         state=NtvSerialSG.start
#     ),
# )

#######################################################################

# async def program_filmbox_arthouse_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'FilmBox Arthouse'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# filmbox_arthouse_channel = Dialog(
#     Window(
#         Const(text='Программа передач FilmBox Arthouse 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_filmbox_arthouse_channel,
#         state=FilmBoxArthouseSG.start
#     ),
# )

######################################################################

# async def program_amedia_hit_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Amedia Hit'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# amedia_hit_channel = Dialog(
#     Window(
#         Const(text='Программа передач Amedia Hit 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_amedia_hit_channel,
#         state=AmediaHitSG.start
#     ),
# )

####################################################################

# async def program_soviet_kino_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Советское кино'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# soviet_kino_channel = Dialog(
#     Window(
#         Const(text='Программа передач Советское кино 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_soviet_kino_channel,
#         state=SovietKinoSG.start
#     ),
# )

#####################################################################

# async def program_o_kino_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'О!Кино'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# o_kino_channel = Dialog(
#     Window(
#         Const(text='Программа передач О!Кино 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_o_kino_channel,
#         state=OKinoSG.start
#     ),
# )

###############################################################

# async def program_viju_serial_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'viju+ Serial'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# viju_serial_channel = Dialog(
#     Window(
#         Const(text='Программа передач viju+ Serial 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_viju_serial_channel,
#         state=VijuSerialSG.start
#     ),
# )

############################################################

# async def program_mosfilm_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Мосфильм. Золотая коллекция'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# mosfilm_channel = Dialog(
#     Window(
#         Const(text='Программа передач Мосфильм. Золотая коллекция 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_mosfilm_channel,
#         state=MosfilmGoldSG.start
#     ),
# )

###############################################################

# async def program_kinojam1_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'KinoJam 1'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kinojam1_channel = Dialog(
#     Window(
#         Const(text='Программа передач KinoJam 1 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kinojam1_channel,
#         state=KinoJam1SG.start
#     ),
# )

################################################################

# async def program_kinojam2_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'KinoJam 2'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kinojam2_channel = Dialog(
#     Window(
#         Const(text='Программа передач KinoJam 2 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kinojam2_channel,
#         state=KinoJam2SG.start
#     ),
# )

###############################################################

# async def program_start_air_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Start Air'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# start_air_channel = Dialog(
#     Window(
#         Const(text='Программа передач Start Air 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_start_air_channel,
#         state=StartAirSG.start
#     ),
# )

############################################################

# async def program_start_world_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Start World'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# start_world_channel = Dialog(
#     Window(
#         Const(text='Программа передач Start World 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_start_world_channel,
#         state=StartWorldSG.start
#     ),
# )

##################################################################

# async def program_ntv_hit_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'НТВ Хит'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# ntv_hit_channel = Dialog(
#     Window(
#         Const(text='Программа передач НТВ Хит 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_ntv_hit_channel,
#         state=NtvHitSG.start
#     ),
# )

##############################################################

# async def program_sapfir_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Сапфир'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# sapfir_channel = Dialog(
#     Window(
#         Const(text='Программа передач Сапфир 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_sapfir_channel,
#         state=SapfirSG.start
#     ),
# )

#################################################################

# async def program_day_win_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'День Победы'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# day_win_channel = Dialog(
#     Window(
#         Const(text='Программа передач День Победы 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_day_win_channel,
#         state=DayWinSG.start
#     ),
# )

#############################################################

# async def program_timeless_dizi_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Timeless Dizi Channel'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# timeless_dizi_channel = Dialog(
#     Window(
#         Const(text='Программа передач Timeless Dizi Channel 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_timeless_dizi_channel,
#         state=TimelessDiziSG.start
#     ),
# )

##############################################################

# async def program_kinoman_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Киноман'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kinoman_channel = Dialog(
#     Window(
#         Const(text='Программа передач Киноман 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kinoman_channel,
#         state=KinomanSG.start
#     ),
# )

############################################################

# async def program_kinomix_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Киномикс'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kinomix_channel = Dialog(
#     Window(
#         Const(text='Программа передач Киномикс 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kinomix_channel,
#         state=KinomixSG.start
#     ),
# )

#########################################################

# async def program_scream_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Scream'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# scream_channel = Dialog(
#     Window(
#         Const(text='Программа передач Scream 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_scream_channel,
#         state=ScreamSG.start
#     ),
# )

#######################################################################

# async def program_criminal_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Криминальное'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# criminal_channel = Dialog(
#     Window(
#         Const(text='Программа передач Криминальное 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_criminal_channel,
#         state=CriminalSG.start
#     ),
# )

####################################################################

# async def program_lovestory_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Лавстори'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# lovestory_channel = Dialog(
#     Window(
#         Const(text='Программа передач Лавстори 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_lovestory_channel,
#         state=LovestorySG.start
#     ),
# )

##################################################################

# async def program_favorite_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Любимое'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# favorite_channel = Dialog(
#     Window(
#         Const(text='Программа передач Любимое 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_favorite_channel,
#         state=FavoriteSG.start
#     ),
# )

####################################################################

# async def program_favorite_kino_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Любимое кино'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# favorite_kino_channel = Dialog(
#     Window(
#         Const(text='Программа передач Любимое кино 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_favorite_kino_channel,
#         state=FavoriteKinoSG.start
#     ),
# )

#################################################################

# async def program_kinoscary_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Киноужас'
#     res = await orm_get_programs(session, program_title)
#     if res:
#         res = "\n".join([f"{row.program_time.strftime('%H:%M')} - {row.program_title}" for row in res])
#     else:
#         res = 'Нет программ на оставшуюся часть дня.'
#     return {'program_title': res}

# kinoscary_channel = Dialog(
#     Window(
#         Const(text='Программа передач Киноужас 👇\n'),
#         Format('{program_title}'),

#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         getter=program_kinoscary_channel,
#         state=KinoScarySG.start
#     ),
# )

####################################################################

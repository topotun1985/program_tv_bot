from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Cancel, ScrollingGroup
from aiogram_dialog.widgets.text import Const
from config_data.tv_channel_utils import create_tv_channel_dialog


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
        Const('🎬 <b>Фильмы и сериалы</b>'),
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

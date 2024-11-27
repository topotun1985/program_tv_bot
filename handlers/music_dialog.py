from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Cancel, Row
from aiogram_dialog.widgets.text import Const
from config_data.tv_channel_utils import create_tv_channel_dialog


class MusicSG(StatesGroup):
    start = State()


class MezzoSG(StatesGroup):
    start = State()


class MusicFirstSG(StatesGroup):
    start = State()


class Mtv80SG(StatesGroup):
    start = State()


class McmTopSG(StatesGroup):
    start = State()


class MusicBoxGoldSG(StatesGroup):
    start = State()


class RuTvSG(StatesGroup):
    start = State()


class TntMusicSG(StatesGroup):
    start = State()


class Mtv00SG(StatesGroup):
    start = State()


class BridgeTvRussianHitSG(StatesGroup):
    start = State()


class EuropaPlusTvSG(StatesGroup):
    start = State()


class BridgeTvSG(StatesGroup):
    start = State()


class LaMinorSG(StatesGroup):
    start = State()


class AivaSG(StatesGroup):
    start = State()


class SongTvRussiaSG(StatesGroup):
    start = State()


class BridgeTvClassicSG(StatesGroup):
    start = State()


class BridgeTvDeluxeSG(StatesGroup):
    start = State()


class BridgeTvHitsSG(StatesGroup):
    start = State()


class BridgeRockSG(StatesGroup):
    start = State()


class WarmSG(StatesGroup):
    start = State()


music_dialog = Dialog(
    Window(
        Const(text='🎧 <b>Музыкальные каналы</b>'),
        Row(
            Start(Const('Mezzo'), id='b_mezzo_ch', state=MezzoSG.start),
            Start(Const('Музыка Первого'),id='b_music_first_ch', state=MusicFirstSG.start),
            Start(Const('MTV 80s'), id='b_mtv80s_ch', state=Mtv80SG.start),
        ),
        Row(
            Start(Const('MCM TOP'), id='b_mcm_top_ch', state=McmTopSG.start),
            Start(Const('Music Box Gold'),id='b_music_box_gold_ch', state=MusicBoxGoldSG.start),
            Start(Const('Ru.TV'), id='b_ru_tv_ch', state=RuTvSG.start),
        ),
        Row(
            Start(Const('ТНТ MUSIC'), id='b_tnt_music_ch', state=TntMusicSG.start),
            Start(Const('MTV 00s'),id='b_mtv00s_ch', state=Mtv00SG.start),
            Start(Const('Bridge TV Русский Хит'), id='b_bridge_tv_russian_hit_ch', state=BridgeTvRussianHitSG.start),
        ),
        Row(
            Start(Const('Europa Plus TV'),id='b_europaplus_tv_ch', state=EuropaPlusTvSG.start),
            Start(Const('BRIDGE TV'), id='b_bridge_tv_ch', state=BridgeTvSG.start),
            Start(Const('Ля-минор. Мой музыкальный'), id='b_la_minor_ch', state=LaMinorSG.start),
        ),
        Row(
            Start(Const('AIVA'), id='b_avia_ch', state=AivaSG.start),
            Start(Const('SONGTV Russia'), id='b_songtv_russia_ch', state=SongTvRussiaSG.start),
            Start(Const('BRIDGE TV CLASSIC'),id='b_bridge_tv_classic_ch', state=BridgeTvClassicSG.start),
        ),
        Row(
            Start(Const('Bridge TV Deluxe'), id='b_bridge_tv_deluxe_ch', state=BridgeTvDeluxeSG.start),
            Start(Const('Bridge TV Hits'), id='b_bridge_tv_hits_ch', state=BridgeTvHitsSG.start),
        ),
        Row(
            Start(Const('Bridge Rock'), id='b_bridge_rock_ch', state=BridgeRockSG.start),
            Start(Const('Жара'), id='b_warm_ch', state=WarmSG.start),
        ),
        Cancel(Const('◀️ Назад'), id='b_cancel'),
        #getter=username_getter,
        state=MusicSG.start
    ),
)


mezzo_channel = create_tv_channel_dialog('Mezzo', MezzoSG.start)
music_first_channel = create_tv_channel_dialog('Музыка Первого', MusicFirstSG.start)
mtv80_channel = create_tv_channel_dialog('MTV 80s', Mtv80SG.start)
mcm_top_channel = create_tv_channel_dialog('MCM TOP', McmTopSG.start)
music_box_gold_channel = create_tv_channel_dialog('Music Box Gold', MusicBoxGoldSG.start)
ru_tv_channel = create_tv_channel_dialog('Ru.TV', RuTvSG.start)
tnt_music_channel = create_tv_channel_dialog('ТНТ MUSIC', TntMusicSG.start)
mtv00_channel = create_tv_channel_dialog('MTV 00s', Mtv00SG.start)
bridge_tv_russian_hit_channel = create_tv_channel_dialog('BRIDGE TV Русский Хит', BridgeTvRussianHitSG.start)
europa_plus_tv_channel = create_tv_channel_dialog('Europa Plus TV', EuropaPlusTvSG.start)
bridge_tv_channel = create_tv_channel_dialog('BRIDGE TV', BridgeTvSG.start)
la_minor_channel = create_tv_channel_dialog('Ля-минор. Мой музыкальный', LaMinorSG.start)
aiva_channel = create_tv_channel_dialog('AIVA', AivaSG.start)
song_tv_russia_channel = create_tv_channel_dialog('SONGTV Russia', SongTvRussiaSG.start)
bridge_tv_classic_channel = create_tv_channel_dialog('BRIDGE TV CLASSIC', BridgeTvClassicSG.start)
bridge_tv_deluxe_channel = create_tv_channel_dialog('BRIDGE TV Deluxe', BridgeTvDeluxeSG.start)
bridge_tv_hits_channel = create_tv_channel_dialog('BRIDGE TV HITS', BridgeTvHitsSG.start)
bridge_rock_channel = create_tv_channel_dialog('BRIDGE ROCK', BridgeRockSG.start)
warm_channel = create_tv_channel_dialog('Жара', WarmSG.start)

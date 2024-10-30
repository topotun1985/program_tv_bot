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


class SportSG(StatesGroup):
    start = State()


class MatchFootball3SG(StatesGroup):
    start = State()


class ExtremeSportsSG(StatesGroup):
    start = State()


class MatchFighterSG(StatesGroup):
    start = State()


class RussianExtremeSG(StatesGroup):
    start = State()


class FootballSG(StatesGroup):
    start = State()


class VijuSport(StatesGroup):
    start = State()


class KhlHdSG(StatesGroup):
    start = State()


class MatchFootball1SG(StatesGroup):
    start = State()


class MatchFootball2SG(StatesGroup):
    start = State()


class BoxTvSG(StatesGroup):
    start = State()


class MatchArenaSG(StatesGroup):
    start = State()


class MatchGameSG(StatesGroup):
    start = State()


class BasketballWorldSG(StatesGroup):
    start = State()


class KickSG(StatesGroup):
    start = State()


class M1GlobalSG(StatesGroup):
    start = State()


class MatchPremiereSG(StatesGroup):
    start = State()


class MatchCountrySG(StatesGroup):
    start = State()


class StartTriumphSG(StatesGroup):
    start = State()


class FightBoxSG(StatesGroup):
    start = State()


class MatchPlannetSG(StatesGroup):
    start = State()


sport_dialog = Dialog(
    Window(
        Const(text='Спорт 👇'),
        Row(
            Start(Const('Матч! Футбол 3'), id='b_match_football3_ch', state=MatchFootball3SG.start),
            Start(Const('Extreme Sports'),id='b_extreme_sports_ch', state=ExtremeSportsSG.start),
            Start(Const('МАТЧ! Боец'), id='b_match_fighter_ch', state=MatchFighterSG.start),
        ),
        Row(
            Start(Const('Русский Экстрим'), id='b_russian_extreme_ch', state=RussianExtremeSG.start),
            Start(Const('Футбол'),id='b_football_ch', state=FootballSG.start),
            Start(Const('viju+ Sport'), id='b_viju_sport_ch', state=VijuSport.start),
        ),
        Row(
            Start(Const('КХЛ HD'), id='b_khl_hd_ch', state=KhlHdSG.start),
            Start(Const('Матч! Футбол 1'),id='b_match_football1_ch', state=MatchFootball1SG.start),
            Start(Const('Матч! Футбол 2'), id='b_match_football2_ch', state=MatchFootball2SG.start),
        ),
        Row(
            Start(Const('Бокс ТВ'), id='b_box_tv_ch', state=BoxTvSG.start),
            Start(Const('Матч! Арена'),id='b_match_arena_ch', state=MatchArenaSG.start),
            Start(Const('Матч! Игра'), id='b_match_game_ch', state=MatchGameSG.start),
        ),
        Row(
            Start(Const('Мир Баскетбола'), id='b_basketball_world_ch', state=BasketballWorldSG.start),
            Start(Const('Удар'),id='b_kick_ch', state=KickSG.start),
            Start(Const('M1 Global'), id='b_m1_global_ch', state=M1GlobalSG.start),
        ),
        Row(
            Start(Const('Матч Премьер'), id='b_match_premeire_ch', state=MatchPremiereSG.start),
            Start(Const('Матч! Страна'),id='b_match_country_ch', state=MatchCountrySG.start),
            Start(Const('Старт Триумф'), id='b_start_triumph_ch', state=StartTriumphSG.start),
        ),
        Row(
            Start(Const('FightBoxт'),id='fight_box', state=FightBoxSG.start),
            Start(Const('Матч! Планета'),id='b_match_plannet_ch', state=MatchPlannetSG.start),
        ),
        Cancel(Const('◀️ Назад'), id='b_cancel'),
        #getter=username_getter,
        state=SportSG.start
    ),
)


match_football3_channel = create_tv_channel_dialog('МАТЧ! Футбол 3', MatchFootball3SG.start)
extreme_sports_channel = create_tv_channel_dialog('Extreme Sports', ExtremeSportsSG.start)
match_fighter_channel = create_tv_channel_dialog('МАТЧ! Боец', MatchFighterSG.start)
russian_extreme_channel = create_tv_channel_dialog('Русский Экстрим', RussianExtremeSG.start)
football_channel = create_tv_channel_dialog('Футбол', FootballSG.start)
viju_sport_channel = create_tv_channel_dialog('viju+ Sport', VijuSport.start)
khl_hd_channel = create_tv_channel_dialog('КХЛ HD', KhlHdSG.start)
match_football1_channel = create_tv_channel_dialog('МАТЧ! Футбол 1', MatchFootball1SG.start)
match_football2_channel = create_tv_channel_dialog('МАТЧ! Футбол 2', MatchFootball2SG.start)
box_tv_channel = create_tv_channel_dialog('Бокс ТВ', BoxTvSG.start)
match_arena_channel = create_tv_channel_dialog('МАТЧ! Арена', MatchArenaSG.start)
match_game_channel = create_tv_channel_dialog('МАТЧ! Игра', MatchGameSG.start)
basketball_world_channel = create_tv_channel_dialog('Мир Баскетбола', BasketballWorldSG.start)
kick_channel = create_tv_channel_dialog('Удар', KickSG.start)
m1_global_channel = create_tv_channel_dialog('M1 Global', M1GlobalSG.start)
match_premiere_channel = create_tv_channel_dialog('МАТЧ! Премьер', MatchPremiereSG.start)
match_country_channel = create_tv_channel_dialog('МАТЧ! Страна', MatchCountrySG.start)
start_triumph_channel = create_tv_channel_dialog('Старт Триумф', StartTriumphSG.start)
fight_box_channel = create_tv_channel_dialog('FightBox', FightBoxSG.start)
match_plannet_channel = create_tv_channel_dialog('МАТЧ! Планета', MatchPlannetSG.start)



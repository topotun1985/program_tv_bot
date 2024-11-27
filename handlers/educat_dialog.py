from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Cancel, ScrollingGroup
from aiogram_dialog.widgets.text import Const
from config_data.tv_channel_utils import create_tv_channel_dialog


class EduSG(StatesGroup):
    start = State()


class HistorySG(StatesGroup):
    start = State()


class MysteryOfGalaxySG(StatesGroup):
    start = State()


class VijuExploreSG(StatesGroup):
    start = State()


class VijuHistorySG(StatesGroup):
    start = State()


class ZooTvSG(StatesGroup):
    start = State()


class MyPlanetSG(StatesGroup):
    start = State()


class TeletravelSG(StatesGroup):
    start = State()


class PetsSG(StatesGroup):
    start = State()


class VijuNatureSG(StatesGroup):
    start = State()


class RussianTravelGuideSG(StatesGroup):
    start = State()


class WhoIsWhoSG(StatesGroup):
    start = State()


class ScienceSG(StatesGroup):
    start = State()


class ZooParkSG(StatesGroup):
    start = State()


class Tv365SG(StatesGroup):
    start = State()


class TravelAdventureSG(StatesGroup):
    start = State()


class EnlightenmentSG(StatesGroup):
    start = State()


class NanoSG(StatesGroup):
    start = State()


class WildLifeSG(StatesGroup):
    start = State()


class LivePlanetSG(StatesGroup):
    start = State()


class HdMediaSG(StatesGroup):
    start = State()


class AdventureHdSG(StatesGroup):
    start = State()


class HunterFishermanSG(StatesGroup):
    start = State()


class WorldAnimalsSG(StatesGroup):
    start = State()


class LetIsGoSG(StatesGroup):
    start = State()


class UnknownPlannetSG(StatesGroup):
    start = State()


class DogAndCoSG(StatesGroup):
    start = State()


class TerraIncognitaSG(StatesGroup):
    start = State()


class WorldAroundHDSG(StatesGroup):
    start = State()


class StarPlusSG(StatesGroup):
    start = State()


class TerraSG(StatesGroup):
    start = State()


class EnglishClubTvSG(StatesGroup):
    start = State()


class MyElementSG(StatesGroup):
    start = State()


class CountryLifeSG(StatesGroup):
    start = State()


educat_dialog = Dialog(
    Window(
        Const(text='📚 <b>Познавательные каналы</b>'),
        ScrollingGroup(
            Start(Const('История'), id='b_history_ch', state=HistorySG.start),
            Start(Const('Тайны Галактики'), id='b_mysteries_of_the_galaxy_ch', state=MysteryOfGalaxySG.start),
            Start(Const('viju Explore'), id='b_viju_explore_ch', state=VijuExploreSG.start),
            Start(Const('viju History'), id='b_viju_history_ch', state=VijuHistorySG.start),
            Start(Const('Зоо ТВ'), id='b_zoo_tv_ch', state=ZooTvSG.start),
            Start(Const('Моя Планета'), id='b_my_planet_ch', state=MyPlanetSG.start),
            Start(Const('Телепутешествия'), id='b_teletravel_ch', state=TeletravelSG.start),
            Start(Const('Домашние животные'), id='b_pets_ch', state=PetsSG.start),
            Start(Const('viju Nature'), id='b_viju_nature_ch', state=VijuNatureSG.start),
            Start(Const('Russian Travel Guide'), id='b_russian_travel_guide_ch', state=RussianTravelGuideSG.start),
            Start(Const('Кто есть кто'), id='b_who_is_wo_ch', state=WhoIsWhoSG.start),
            Start(Const('Наука'), id='b_science_ch', state=ScienceSG.start),
            Start(Const('Zooпарк'), id='b_zoopark_ch', state=ZooParkSG.start),
            Start(Const('365 дней ТВ'), id='b_365_days_tv_ch', state=Tv365SG.start),
            Start(Const('Travel+ Adventure'), id='b_travel_plus_adventure_ch', state=TravelAdventureSG.start),
            Start(Const('Просвещение'), id='b_enlightenment_ch', state=EnlightenmentSG.start),
            Start(Const('Нано'), id='b_nano_ch', state=NanoSG.start),
            Start(Const('Живая природа'), id='b_wildlife_ch', state=WildLifeSG.start),
            Start(Const('Живая планета'), id='b_live_planet_ch', state=LivePlanetSG.start),
            Start(Const('HD Медиа'), id='b_hd_media_ch', state=HdMediaSG.start),
            Start(Const('Приключения HD'), id='b_adventures_hd_ch', state=AdventureHdSG.start),
            Start(Const('Охотник и Рыболов HD'), id='b_hunter_and_fisherman_ch', state=HunterFishermanSG.start),
            Start(Const('В мире животных'), id='b_In_the_world_of_animals_ch', state=WorldAnimalsSG.start),
            Start(Const('Поехали!'), id='b_let_is_go_ch', state=LetIsGoSG.start),
            Start(Const('Неизвестная Планета'), id='b_unknown_plannet_ch', state=UnknownPlannetSG.start),
            Start(Const('Пёс и Ко'), id='b_dog_and_co_ch', state=DogAndCoSG.start),
            Start(Const('Терра Инкогнита'), id='b_terra_incognito_ch', state=TerraIncognitaSG.start),
            Start(Const('Мир вокруг HD'), id='b_world_around_ch', state=WorldAroundHDSG.start),
            Start(Const('Звезда Плюс'), id='b_star_plus_ch', state=StarPlusSG.start),
            Start(Const('TERRA'), id='b_terra_ch', state=TerraSG.start),
            Start(Const('English Club TV'), id='b_english_club_tv_ch', state=EnglishClubTvSG.start),
            Start(Const('Моя стихия'), id='b_my_element_ch', state=MyElementSG.start),
            Start(Const('Загородная жизнь'), id='b_country_life_ch', state=CountryLifeSG.start),
            id='channel_group_2',
            width=3,
            height=6
        ),
        Cancel(Const('◀️ Назад'), id='b_cancel'),
        #getter=username_getter,
        state=EduSG.start
    ),
)


history_channel = create_tv_channel_dialog('История', HistorySG.start)
mystery_galaxy_channel = create_tv_channel_dialog('Тайны галактики', MysteryOfGalaxySG.start)
viju_explore_channel = create_tv_channel_dialog('viju Explore', VijuExploreSG.start)
viju_history_channel = create_tv_channel_dialog('viju History', VijuHistorySG.start)
zoo_tv_channel = create_tv_channel_dialog('Зоо ТВ', ZooTvSG.start)
my_planet_channel = create_tv_channel_dialog('Моя Планета', MyPlanetSG.start)
teletravel_channel = create_tv_channel_dialog('Телепутешествия', TeletravelSG.start)
pets_channel = create_tv_channel_dialog('Домашние животные', PetsSG.start)
viju_nature_channel = create_tv_channel_dialog('viju Nature', VijuNatureSG.start)
russian_travel_guide_channel = create_tv_channel_dialog('Russian Travel Guide', RussianTravelGuideSG.start)
who_is_who_channel = create_tv_channel_dialog('Кто есть кто', WhoIsWhoSG.start)
science_channel = create_tv_channel_dialog('Наука', ScienceSG.start)
zoopark_channel = create_tv_channel_dialog('Zooпарк', ZooParkSG.start)
tv365_channel = create_tv_channel_dialog('365 дней ТВ', Tv365SG.start)
travel_adventure_channel = create_tv_channel_dialog('Travel+Adventure', TravelAdventureSG.start)
enlightenment_channel = create_tv_channel_dialog('Просвещение', EnlightenmentSG.start)
nano_channel = create_tv_channel_dialog('Нано', NanoSG.start)
wildlife_channel = create_tv_channel_dialog('Живая природа', WildLifeSG.start)
live_planet_channel = create_tv_channel_dialog('Живая планета', LivePlanetSG.start)
hd_media_channel = create_tv_channel_dialog('HD Медиа', HdMediaSG.start)
adventure_hd_channel = create_tv_channel_dialog('Приключения HD', AdventureHdSG.start)
hunter_fisherman_channel = create_tv_channel_dialog('Охотник и Рыболов HD', HunterFishermanSG.start)
world_animal_channel = create_tv_channel_dialog('В мире животных', WorldAnimalsSG.start)
let_is_go_channel = create_tv_channel_dialog('Поехали!', LetIsGoSG.start)
unknown_plannet_channel = create_tv_channel_dialog('Неизвестная Планета', UnknownPlannetSG.start)
dog_and_co_channel = create_tv_channel_dialog('Пес и Ко', DogAndCoSG.start)
terra_incognita_channel = create_tv_channel_dialog('Терра Инкогнита', TerraIncognitaSG.start)
world_around_hd_channel = create_tv_channel_dialog('Мир вокруг HD', WorldAroundHDSG.start)
star_plus_channel = create_tv_channel_dialog('Звезда Плюс', StarPlusSG.start)
terra_channel = create_tv_channel_dialog('Terra', TerraSG.start)
english_club_tv_channel = create_tv_channel_dialog('English Club TV', EnglishClubTvSG.start)
my_element_channel = create_tv_channel_dialog('Моя стихия', MyElementSG.start)
country_life_channel = create_tv_channel_dialog('Загородная жизнь', CountryLifeSG.start)

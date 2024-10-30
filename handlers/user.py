# from aiogram import Bot, Dispatcher, Router, F
# from aiogram.client.default import DefaultBotProperties
# from aiogram.enums import ParseMode
# from aiogram.filters import Command
# from aiogram.fsm.state import State, StatesGroup
# from aiogram.types import CallbackQuery, Message, User
# from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
# from aiogram_dialog.widgets.kbd import Start, Next, Back, Cancel, SwitchTo, ScrollingGroup, Button, Row, Select, Group, Checkbox, ManagedCheckbox
# from aiogram_dialog.widgets.text import Const, Format, List, Multi
# from database.orm_query import orm_get_programs, orm_get_program
# from sqlalchemy.ext.asyncio import AsyncSession
# from datetime import datetime


# user_router = Router()


# @user_router.message(Command('help'))
# async def process_help_command(message: Message):
#     await message.answer('What do you want??')


# class MainMenuSG(StatesGroup):
#     start = State()


# class FedChanSG(StatesGroup):
#     start = State()


# class FirstChannel(StatesGroup):
#     start = State()


# class RussiaOneChannel(StatesGroup):
#     start = State()


# class MatchTvChannel(StatesGroup):
#     start = State()


# class NtvChannel(StatesGroup):
#     start = State()


# class FiveTvChannel(StatesGroup):
#     start = State()


# class TvCenterChannel(StatesGroup):
#     start = State()


# class CultureChannel(StatesGroup):
#     start = State()


# class StsChannel(StatesGroup):
#     start = State()


# class RenTvChannel(StatesGroup):
#     start = State()


# class OtpChannel(StatesGroup):
#     start = State()


# class TntChannel(StatesGroup):
#     start = State()


# class HomeChannel(StatesGroup):
#     start = State()


# class FridayChannel(StatesGroup):
#     start = State()


# class Tv3Channel(StatesGroup):
#     start = State()


# class MuzTvChannel(StatesGroup):
#     start = State()


# class CarouselChannel(StatesGroup):
#     start = State()


# class StarChannel(StatesGroup):
#     start = State()


# class CheChannel(StatesGroup):
#     start = State()


# class MirChannel(StatesGroup):
#     start = State()


# class SpasChannel(StatesGroup):
#     start = State()


# class YouChannel(StatesGroup):
#     start = State()


# class Russia24Channel(StatesGroup):
#     start = State()


# class FilmSG(StatesGroup):
#     start = State()


# class EduSG(StatesGroup):
#     start = State()


# class SportSG(StatesGroup):
#     start = State()


# class ChildSG(StatesGroup):
#     start = State()


# class InfoSG(StatesGroup):
#     start = State()


# class MusicSG(StatesGroup):
#     start = State()


# class HobbieSG(StatesGroup):
#     start = State()


# class EntertainSG(StatesGroup):
#     start = State()


# class HdSG(StatesGroup):
#     start = State()


# class AdultSG(StatesGroup):
#     start = State()


# async def username_getter(dialog_manager: DialogManager, event_from_user: User, **kwargs):
#     return {'username': event_from_user.username or 'Stranger'}

#######################################################################################################

# start_dialog = Dialog(
#     Window(
#         Format('<b>Привет, {username}!</b>\n'),
#         Const('Нажми на кнопку,\nчтобы перейти во второй диалог 👇'),
#         Row(
#             Start(Const('Общероссийские'),id='b_main_menu', state=FedChanSG.start),
#             Start(Const('Фильмы и сериалы'), id='b_film', state=FilmSG.start),
#             Start(Const('Познавательные'), id='b_educat', state=EduSG.start),
#         ),
#         Row(
#             Start(Const('Спорт'),id='b_sport', state=SportSG.start),
#             Start(Const('Детям'), id='b_children', state=ChildSG.start),
#             Start(Const('Информация'), id='b_info', state=InfoSG.start),
#         ),
#         Row(
#             Start(Const('Музыка'),id='b_music', state=MusicSG.start),
#             Start(Const('Увлечения'), id='b_hobbie', state=HobbieSG.start),
#             Start(Const('Развлечения'), id='b_entertain', state=EntertainSG.start),
#         ),
#         Row(
#             Start(Const('HD'),id='b_hd', state=HdSG.start),
#             Start(Const('18+'), id='b_adult', state=AdultSG.start),
#         ),
#         Start(Const('Избранные ❤️'), id='go_second', state=FedChanSG.start),
#         getter=username_getter,
#         state=MainMenuSG.start
#     ),
# )

# #######################################################################################################

# fed_dialog = Dialog(
#     Window(
#         #Format('<b>Привет, {username}!</b>\n'),
#         Const('Общероссийские каналы 👇'),
#         Row(
#             Start(Const('Первый'),id='b_first_ch', state=FirstChannel.start),
#             #Button(Const('Первый'),id='b_first_ch', on_click='first_channel'),
#             Start(Const('Россия 1'), id='b_rus1_ch', state=RussiaOneChannel.start),
#             Start(Const('Матч'), id='b_match_ch', state=MatchTvChannel.start),
#         ),
#         Row(
#             Start(Const('НТВ'),id='b_ntv_ch', state=NtvChannel.start),
#             Start(Const('Пятый'), id='b_five_ch', state=FiveTvChannel.start),
#             Start(Const('Культура'), id='b_culture_ch', state=CultureChannel.start),
#         ),
#         Row(
#             Start(Const('Карусель'),id='b_carousel_ch', state=CarouselChannel.start),
#             Start(Const('ОТР'), id='b_otr_ch', state=OtpChannel.start),
#             Start(Const('ТВ Центр'), id='b_center_ch', state=TvCenterChannel.start),
#         ),
#         Row(
#             Start(Const('РЕН ТВ'),id='b_rentv_ch', state=RenTvChannel.start),
#             Start(Const('Спас ТВ'), id='b_spastv_ch', state=SpasChannel.start),
#             Start(Const('СТС'), id='b_sts_ch', state=StsChannel.start),
#         ),
#         Row(
#             Start(Const('Домашний'),id='b_housetv_ch', state=HomeChannel.start),
#             Start(Const('ТВ-3'), id='b_tv3_ch', state=Tv3Channel.start),
#             Start(Const('Пятница'), id='b_fridaytv_ch', state=FridayChannel.start),
#         ),
#         Row(
#             Start(Const('Звезда'),id='b_starttv_ch', state=StarChannel.start),
#             Start(Const('МИР'), id='b_mirtv_ch', state=MirChannel.start),
#             Start(Const('ТНТ'), id='b_tnt_ch', state=TntChannel.start),
#         ),
#         Row(
#             Start(Const('МУЗ-ТВ'),id='b_muztv_ch', state=MuzTvChannel.start),
#             Start(Const('Че'), id='b_che_ch', state=CheChannel.start),
#             Start(Const('Ю'), id='b_you_ch', state=YouChannel.start),
#         ),
#         Row(
#             Start(Const('Россия 24'), id='b_russia24_ch', state=Russia24Channel.start)
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=FedChanSG.start
#     ),
# )

#######################################################################################################

# film_dialog = Dialog(
#     Window(
#         #Format('<b>Привет, {username}!</b>\n'),
#         Const('Фильмы и сериалы 👇'),
#         ScrollingGroup(
#             Button(Const('Кино ТВ'),id='b_kinotv_ch', on_click=''),
#             Button(Const('А2'), id='b_a2_ch', on_click=''),
#             Button(Const('.Black'), id='b_black_ch', on_click=''),
#             Button(Const('.Sci-fi'),id='b_sci_ch', on_click=''),
#             Button(Const('Hollywood'), id='b_hollywood_ch', on_click=''),
#             Button(Const('viju TV1000'), id='b_viju1000_ch', on_click=''),
#             Button(Const('viju TV1000 русское'),id='b_viju1000rus_ch', on_click=''),
#             Button(Const('ТВ21'), id='b_tv21_ch', on_click=''),
#             Button(Const('Дом Кино'), id='b_domkino_ch', on_click=''),
#             Button(Const('Иллюзион +'),id='b_illuzion_ch', on_click=''),
#             Button(Const('Индийское кино'), id='b_indian_ch', on_click=''),
#             Button(Const('Киносвидание'), id='b_kinodate_ch', on_click=''),
#             Button(Const('Кинохит'),id='b_kinohit_ch', on_click=''),
#             Button(Const('НСТ'), id='b_nst_ch', on_click=''),
#             Button(Const('Родное кино'), id='b_native_kino_ch', on_click=''),
#             Button(Const('Наше новое кино'),id='b_our_new_kino_ch', on_click=''),
#             Button(Const('Русский Иллюзион'), id='b_rus_illuzion_ch', on_click=''),
#             Button(Const('Кинопремьера'), id='b_kinopremier_ch', on_click=''),
#             Button(Const('Феникс+ Кино'),id='b_fenix_kino_ch', on_click=''),
#             Button(Const('FOX'), id='b_fox_ch', on_click=''),
#             Button(Const('FOX Life'), id='b_fox_life_ch', on_click=''),
#             Button(Const('Еврокино'),id='b_eurokino_ch', on_click=''),
#             Button(Const('Индия'), id='b_india_ch', on_click=''),
#             Button(Const('Мир сериала'), id='b_mir_serial_ch', on_click=''),
#             Button(Const('viju TV1000 action'),id='b_viju1000_action_ch', on_click=''),
#             Button(Const('РТВ - Любимое кино'), id='b_favorite_kino_ch', on_click=''),
#             Button(Const('.Red'), id='b_red_ch', on_click=''),
#             Button(Const('Киносерия'),id='b_kinoseria_ch', on_click=''),
#             Button(Const('Кинокомедиа'), id='b_kinocomedy_ch', on_click=''),
#             Button(Const('Русский роман'), id='b_rus_roman_ch', on_click=''),
#             Button(Const('Русский бестселлер'),id='b_rus_bestseller_ch', on_click=''),
#             Button(Const('A1'), id='b_a1_ch', on_click=''),
#             Button(Const('Русский детектив'), id='b_rus_detectiev_ch', on_click=''),
#             Button(Const('Мужское кино'),id='b_men_kino_ch', on_click=''),
#             Button(Const('Комедия'), id='b_comedy_ch', on_click=''),
#             Button(Const('viju+ Comedy'), id='b_viju_comedy_ch', on_click=''),
#             Button(Const('viju+ Megahit'),id='b_viju_megahit_ch', on_click=''),
#             Button(Const('viju+ Premiere'), id='b_viju_premiere_ch', on_click=''),
#             Button(Const('Fox HD'), id='b_fox_hd_ch', on_click=''),
#             Button(Const('Sony ТВ HD'),id='b_sony_tv_ch', on_click=''),
#             Button(Const('Hollywood HD'), id='b_hollywood_ch', on_click=''),
#             Button(Const('Шокирующее'), id='b_shock_tv_ch', on_click=''),
#             Button(Const('Комедийное'),id='b_comedytv_ch', on_click=''),
#             Button(Const('Fox Life HD'), id='b_fox_life_hd_ch', on_click=''),
#             Button(Const('Amedia Premium HD'), id='b_amedia_premium_hd_ch', on_click=''),
#             Button(Const('Страшное HD'),id='b_scary_hd__ch', on_click=''),
#             Button(Const('Bollywood HD '), id='b_bollywood_hd_ch', on_click=''),
#             Button(Const('Премиальное'), id='b_premium_tv_ch', on_click=''),
#             Button(Const('Остросюжетное HD'),id='b_spicy_tv_ch', on_click=''),
#             Button(Const('Cinema'), id='b_cinema_tv_ch', on_click=''),
#             Button(Const('Paramount Channel'), id='b_paramount_ch', on_click=''),
#             Button(Const('Дом Кино Премиум'),id='b_home_kino_premium_ch', on_click=''),
#             Button(Const('Наше HD'), id='b_our_hd_ch', on_click=''),
#             Button(Const('Душевное'), id='b_soul_tv_ch', on_click=''),
#             Button(Const('НТВ Сериал'),id='b_ntv_serial_ch', on_click=''),
#             Button(Const('FilmBox HD'), id='b_filmbox_ch', on_click=''),
#             Button(Const('Мужское кино HD'), id='b_men_kino_hd_ch', on_click=''),
#             Button(Const('FilmBox Arthouse'),id='b_filmbox_arthouse_ch', on_click=''),
#             Button(Const('Amedia Hit'), id='b_amedia_hit_ch', on_click=''),
#             Button(Const('Советское кино'), id='b_soviet_kino_ch', on_click=''),
#             Button(Const('О, Кино!'),id='b_o_kino_ch', on_click=''),
#             Button(Const('viju+ Serial'), id='b_viju_serial_ch', on_click=''),
#             Button(Const('Мосфильм. Золотая коллекция'), id='b_mosfilm_ch', on_click=''),
#             Button(Const('KinoJam 1'),id='b_kinojam1_ch', on_click=''),
#             Button(Const('KinoJam 2'), id='b_kinojam2_ch', on_click=''),
#             Button(Const('START Air'), id='b_start_air_ch', on_click=''),
#             Button(Const('START World'),id='b_start_world_ch', on_click=''),
#             Button(Const('НТВ Хит'), id='b_ntv_hit_ch', on_click=''),
#             Button(Const('Сапфир'), id='b_sapfir_ch', on_click=''),
#             Button(Const('DetectiveJam'),id='b_detectivejam_ch', on_click=''),
#             Button(Const('FamilyJam'), id='b_familyjam_ch', on_click=''),
#             Button(Const('День Победы'), id='b_day_win_ch', on_click=''),
#             Button(Const('Драма HD'),id='b_drama_hd_ch', on_click=''),
#             Button(Const('Timeless Dizi Channel'), id='b_timeless_dizzi_ch', on_click=''),
#             Button(Const('Киноман'), id='b_kinoman_ch', on_click=''),
#             Button(Const('Киномикс'),id='b_kinomix_ch', on_click=''),
#             Button(Const('Romance'), id='b_romance_ch', on_click=''),
#             Button(Const('Suspense'), id='b_suspense_ch', on_click=''),
#             Button(Const('VHS'),id='b_vhs_ch', on_click=''),
#             Button(Const('KIONХИТ'), id='b_kionhit_ch', on_click=''),
#             Button(Const('Scream'), id='b_scream_ch', on_click=''),
#             Button(Const('Криминальное'),id='b_criminal_ch', on_click=''),
#             Button(Const('Лавстори'), id='b_lovestory_ch', on_click=''),
#             Button(Const('Любимое'), id='b_favorite_ch', on_click=''),
#             id='channels_group_1',
#             width=3,
#             height=7
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=FilmSG.start
#     ),
# )

# #######################################################################################################

# educat_dialog = Dialog(
#     Window(
#         Const(text='Познавательные 👇'),
#         ScrollingGroup(
#             Button(Const('История'), id='b_history_ch', on_click=''),
#             Button(Const('Тайны Галактики'),id='b_mysteries_of_the_galaxy_ch', on_click=''),
#             Button(Const('Discovery Восточная Европа'), id='b_discovery_eastern_europe_ch', on_click=''),
#             Button(Const('Animal Planet'), id='b_animal_planet_ch', on_click=''),
#             Button(Const('Discovery Channel'),id='b_discovery_channel_ch', on_click=''),
#             Button(Const('Discovery Science'), id='b_discovery_science_ch', on_click=''),
#             Button(Const('National Geographic'), id='b_National_geographic_ch', on_click=''),
#             Button(Const('Океан HD'),id='b_ocean_hd_ch', on_click=''),
#             Button(Const('viju Explore'), id='b_viju_explore_ch', on_click=''),
#             Button(Const('viju History'), id='b_viju_history_ch', on_click=''),
#             Button(Const('Время'),id='b_time_ch', on_click=''),
#             Button(Const('Зоо ТВ'), id='b_zoo_tv_ch', on_click=''),
#             Button(Const('Моя Планета'), id='b_my_planet_ch', on_click=''),
#             Button(Const('Телепутешествия'),id='b_teletravel_ch', on_click=''),
#             Button(Const('Домашние животные'), id='b_pets_ch', on_click=''),
#             Button(Const('viju Nature'), id='b_viju_nature_ch', on_click=''),
#             Button(Const('Russian Travel Guide'),id='b_russian_travel_guide_ch', on_click=''),
#             Button(Const('Кто есть кто'), id='b_who_is_wo_ch', on_click=''),
#             Button(Const('Наука'), id='b_science_ch', on_click=''),
#             Button(Const('Zooпарк'),id='b_zoopark_ch', on_click=''),
#             Button(Const('365 дней ТВ'), id='b_365_days_tv_ch', on_click=''),
#             Button(Const('Travel+ Adventure'), id='b_travel_plus_adventure_ch', on_click=''),
#             Button(Const('Просвещение'),id='b_enlightenment_ch', on_click=''),
#             Button(Const('Нано'), id='b_nano_ch', on_click=''),
#             Button(Const('Travel Channel'), id='b_travel_channel_ch', on_click=''),
#             Button(Const('Живая природа'),id='b_wildlife_ch', on_click=''),
#             Button(Const('Т24'), id='b_t24_ch', on_click=''),
#             Button(Const('Живая планета'), id='b_live_planet_ch', on_click=''),
#             Button(Const('DTX!'),id='b_dtx_ch', on_click=''),
#             Button(Const('Travel+ Adventure HD'), id='b_travel_plus_adventure_hd_ch', on_click=''),
#             Button(Const('HD Медиа'), id='b_hd_media_ch', on_click=''),
#             Button(Const('National Geographic HD'),id='b_national_geographic_hd_ch', on_click=''),
#             Button(Const('Приключения HD'), id='b_kinojam2_ch', on_click=''),
#             Button(Const('Travel Channel HD'), id='b_adventures_hd_ch', on_click=''),
#             Button(Const('Охотник и Рыболов HD'),id='b_hunter_and_fisherman_ch', on_click=''),
#             Button(Const('В мире животных'), id='b_In_the_world_of_animals_ch', on_click=''),
#             Button(Const('RТД'), id='b_rtd_ch', on_click=''),
#             Button(Const('DocuBox HD'),id='b_docubox_hd_ch', on_click=''),
#             Button(Const('Поехали!'), id='b_let_is_go_ch', on_click=''),
#             Button(Const('Неизвестная Планета'), id='b_unknown_planet_ch', on_click=''),
#             Button(Const('RT Doc'),id='b_rt_doc_ch', on_click=''),
#             Button(Const('Пёс и Ко'), id='b_dog_and_co_ch', on_click=''),
#             Button(Const('Терра Инкогнита'), id='b_terra_incognito_ch', on_click=''),
#             Button(Const('Мир вокруг'),id='b_world_around_ch', on_click=''),
#             Button(Const('Звезда Плюс'), id='b_star_plus_ch', on_click=''),
#             Button(Const('TERRA'), id='b_terra_ch', on_click=''),
#             Button(Const('CuriosityStream'),id='b_curiosityStream_ch', on_click=''),
#             Button(Const('English Class HD'), id='b_english_class_hd_ch', on_click=''),
#             Button(Const('Моя стихия'), id='b_my_element_ch', on_click=''),
#             Button(Const('Загородная жизнь HD'),id='b_country_life_hd_ch', on_click=''),
#             Button(Const('Неизвестная Россия'), id='b_unknown_russia_ch', on_click=''),
#             Button(Const('Конгресс ТВ'), id='b_congress_tv_ch', on_click=''),
#             id='channel_group_2',
#             width=3,
#             height=6
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=EduSG.start
#     ),
# )

# #############################################################################

# sport_dialog = Dialog(
#     Window(
#         Const(text='Спорт 👇'),
#         Row(
#             Button(Const('Матч! Футбол 3'), id='b_history_ch', on_click=''),
#             Button(Const('Extreme'),id='b_mysteries_of_the_galaxy_ch', on_click=''),
#             Button(Const('Матч! Боец'), id='b_discovery_eastern_europe_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Russian Extreme'), id='b_animal_planet_ch', on_click=''),
#             Button(Const('Футбол'),id='b_discovery_channel_ch', on_click=''),
#             Button(Const('viju+ Sport'), id='b_discovery_science_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('KHL'), id='b_National_geographic_ch', on_click=''),
#             Button(Const('Матч! Футбол 1'),id='b_ocean_hd_ch', on_click=''),
#             Button(Const('Матч! Футбол 2'), id='b_viju_explore_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Бокс ТВ'), id='b_viju_history_ch', on_click=''),
#             Button(Const('Матч! Арена'),id='b_time_ch', on_click=''),
#             Button(Const('Матч! Игра'), id='b_zoo_tv_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Fuel TV HD'), id='b_my_planet_ch', on_click=''),
#             Button(Const('Fast & Fun Box HD'),id='b_teletravel_ch', on_click=''),
#             Button(Const('Мотоспорт ТВ'), id='b_pets_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Матч Премьер'), id='b_viju_nature_ch', on_click=''),
#             Button(Const('Матч! Страна'),id='b_russian_travel_guide_ch', on_click=''),
#             Button(Const('Q Sport'), id='b_who_is_wo_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Старт Триумф'), id='b_science_ch', on_click=''),
#             Button(Const('Окко.Спорт'),id='b_zoopark_ch', on_click=''),
#             Button(Const('Матч! Планета'),id='b_zoopark_ch', on_click=''),
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=SportSG.start
#     ),
# )

# ############################################################################

# child_dialog = Dialog(
#     Window(
#         Const(text='Детям 👇'),
#         ScrollingGroup(
#             Button(Const('Boomerang'), id='b_history_ch', on_click=''),
#             Button(Const('Cartoon Network'),id='b_mysteries_of_the_galaxy_ch', on_click=''),
#             Button(Const('Уникум'), id='b_discovery_eastern_europe_ch', on_click=''),
#             Button(Const('Da Vinci'), id='b_animal_planet_ch', on_click=''),
#             Button(Const('Gulli Girl'),id='b_discovery_channel_ch', on_click=''),
#             Button(Const('JimJam'), id='b_discovery_science_ch', on_click=''),
#             Button(Const('Мультиландия'), id='b_National_geographic_ch', on_click=''),
#             Button(Const('TiJi'),id='b_ocean_hd_ch', on_click=''),
#             Button(Const('Мульт'), id='b_viju_explore_ch', on_click=''),
#             Button(Const('Рыжий'), id='b_viju_history_ch', on_click=''),
#             Button(Const('О!'),id='b_time_ch', on_click=''),
#             Button(Const('Любимое.ТВ'), id='b_zoo_tv_ch', on_click=''),
#             Button(Const('Детский мир'), id='b_my_planet_ch', on_click=''),
#             Button(Const('Смайлик ТВ'),id='b_teletravel_ch', on_click=''),
#             Button(Const('Советские мультфильмы'), id='b_pets_ch', on_click=''),
#             Button(Const('Сказки Зайки'), id='b_viju_nature_ch', on_click=''),
#             Button(Const('Детский телеканал Мультимания'),id='b_russian_travel_guide_ch', on_click=''),
#             Button(Const('Детское кино'), id='b_who_is_wo_ch', on_click=''),
#             Button(Const('Ani'), id='b_science_ch', on_click=''),
#             Button(Const('FAN'),id='b_zoopark_ch', on_click=''),
#             Button(Const('Мультимузыка'), id='b_365_days_tv_ch', on_click=''),
#             Button(Const('СуперГерои'), id='b_travel_plus_adventure_ch', on_click=''),
#             Button(Const('Лёва'),id='b_enlightenment_ch', on_click=''),
#             Button(Const('Baby Time'), id='b_nano_ch', on_click=''),
#             Button(Const('KidsTV'), id='b_travel_channel_ch', on_click=''),
#             Button(Const('DuckTV'),id='b_wildlife_ch', on_click=''),
#             Button(Const('Sumiko'), id='b_t24_ch', on_click=''),
#             Button(Const('Cartoon Classics'), id='b_live_planet_ch', on_click=''),
#             Button(Const('Чижик!'),id='b_dtx_ch', on_click=''),
#             Button(Const('ТипТоп'), id='b_travel_plus_adventure_hd_ch', on_click=''),
#             Button(Const('Пингвин'), id='b_hd_media_ch', on_click=''),
#             id='channel_group_3',
#             width=3,
#             height=6
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=ChildSG.start
#     ),
# )

# ############################################################################

# info_dialog = Dialog(
#     Window(
#         Const(text='Информация 👇'),
#         Row(
#             Button(Const('RTVI'), id='b_rtvi_ch', on_click=''),
#             Button(Const('NHK World Japan'),id='b_nhk_world_japan_ch', on_click=''),
#             Button(Const('Bloomberg'), id='b_bloomberg_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('BBC News'), id='b_bbc_news_ch', on_click=''),
#             Button(Const('CNN'),id='b_cnn_ch', on_click=''),
#             Button(Const('Deutsche Welle'), id='b_deutsche_welle_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Евроновости'), id='b_euronews_ch', on_click=''),
#             Button(Const('TV5-Monde'),id='b_tv5_monde_ch', on_click=''),
#             Button(Const('РБК'), id='b_rbk_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('BBC'), id='b_bbc_ch', on_click=''),
#             Button(Const('CNBC'),id='b_cnbc_ch', on_click=''),
#             Button(Const('France 24'), id='b_france24_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('RT'), id='b_my_rt_ch', on_click=''),
#             Button(Const('ЧП.Info'),id='b_chp_info_ch', on_click=''),
#             Button(Const('МИР 24'), id='b_world24_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Башкортостан 24'), id='b_bashkortostan24_ch', on_click=''),
#             Button(Const('360 Новости'),id='b_360news_ch', on_click=''),
#             Button(Const('24KZ'), id='b_2kz_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('ЭХО Москвы'), id='b_echo_moscow_ch', on_click=''),
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=InfoSG.start
#     ),
# )

# ##############################################################################

# music_dialog = Dialog(
#     Window(
#         Const(text='Музыка 👇'),
#         ScrollingGroup(
#             Button(Const('Mezzo'), id='b_mezzo_ch', on_click=''),
#             Button(Const('Музыка Первого'),id='b_music_of_first_ch', on_click=''),
#             Button(Const('MTV 80s'), id='b_mtv80s_ch', on_click=''),
#             Button(Const('MCM TOP'), id='b_mcm_top_ch', on_click=''),
#             Button(Const('Music Box Gold'),id='b_music_box_gold_ch', on_click=''),
#             Button(Const('RU TV'), id='b_ru_tv_ch', on_click=''),
#             Button(Const('ТНТ Music'), id='b_tnt_music_ch', on_click=''),
#             Button(Const('MTV 00s'),id='b_mtv00s_ch', on_click=''),
#             Button(Const('Bridge TV Русский Хит'), id='b_bridge_tv_russian_hit_ch', on_click=''),
#             Button(Const('Шансон-ТВ'), id='b_shanson_tv_ch', on_click=''),
#             Button(Const('Europa Plus TV'),id='b_europaplus_tv_ch', on_click=''),
#             Button(Const('Bridge TV'), id='b_bridge_tv_ch', on_click=''),
#             Button(Const('Ля-минор. Мой музыкальный'), id='b_la_minor_ch', on_click=''),
#             Button(Const('Club MTV'),id='b_club_mtv_ch', on_click=''),
#             Button(Const('MTV Hits International'), id='b_mtv_hits_international_ch', on_click=''),
#             Button(Const('MTV 90s'), id='b_mtv90s_ch', on_click=''),
#             Button(Const('FreshTV'),id='b_freshtv_ch', on_click=''),
#             Button(Const('МузСоюз'), id='b_muzsouz_ch', on_click=''),
#             Button(Const('Aiva'), id='b_avia_ch', on_click=''),
#             Button(Const('SongTV Armenid'),id='b_songtv_armenid_ch', on_click=''),
#             Button(Const('SONGTV Georgia'), id='b_songtv_georgia_ch', on_click=''),
#             Button(Const('SONGTV Russia'), id='b_songtv_russia_ch', on_click=''),
#             Button(Const('Bridge TV Classic'),id='b_bridge_tv_classic_ch', on_click=''),
#             Button(Const('Bridge TV Deluxe'), id='b_bridge_tv_deluxe_ch', on_click=''),
#             Button(Const('Bridge TV Hits'), id='b_bridge_tv_hits_ch', on_click=''),
#             Button(Const('Plan B'),id='b_plan_b__ch', on_click=''),
#             Button(Const('Bridge Rock'), id='b_bridge_rock_ch', on_click=''),
#             Button(Const('MIXM'), id='b_mixm_ch', on_click=''),
#             id='channel_group_4',
#             width=3,
#             height=6
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=MusicSG.start
#     ),
# )

# ############################################################################

# hobbie_dialog = Dialog(
#     Window(
#         Const(text='Увлечения 👇'),
#         ScrollingGroup(
#             Button(Const('Про Бизнес'), id='b_history_ch', on_click=''),
#             Button(Const('Fashion TV'),id='b_mysteries_of_the_galaxy_ch', on_click=''),
#             Button(Const('World Fashion Channel'), id='b_discovery_eastern_europe_ch', on_click=''),
#             Button(Const('Охота и Рыбалка'), id='b_animal_planet_ch', on_click=''),
#             Button(Const('Телекафе'),id='b_discovery_channel_ch', on_click=''),
#             Button(Const('Усадьба'), id='b_discovery_science_ch', on_click=''),
#             Button(Const('Психология 21'), id='b_National_geographic_ch', on_click=''),
#             Button(Const('Успех'),id='b_ocean_hd_ch', on_click=''),
#             Button(Const('Оружие'), id='b_viju_explore_ch', on_click=''),
#             Button(Const('Загородный'), id='b_viju_history_ch', on_click=''),
#             Button(Const('Загородная жизнь'),id='b_time_ch', on_click=''),
#             Button(Const('Тонус'), id='b_zoo_tv_ch', on_click=''),
#             Button(Const('Рыболов'), id='b_my_planet_ch', on_click=''),
#             Button(Const('TLC'),id='b_teletravel_ch', on_click=''),
#             Button(Const('Драйв'), id='b_pets_ch', on_click=''),
#             Button(Const('Здоровое ТВ'), id='b_viju_nature_ch', on_click=''),
#             Button(Const('Живи!'),id='b_russian_travel_guide_ch', on_click=''),
#             Button(Const('Кухня'), id='b_who_is_wo_ch', on_click=''),
#             Button(Const('Авто Плюс'), id='b_science_ch', on_click=''),
#             Button(Const('Еда'),id='b_zoopark_ch', on_click=''),
#             Button(Const('World Business Channel'), id='b_365_days_tv_ch', on_click=''),
#             Button(Const('RTG International'), id='b_travel_plus_adventure_ch', on_click=''),
#             Button(Const('Бобер'),id='b_enlightenment_ch', on_click=''),
#             Button(Const('Конный мир'), id='b_nano_ch', on_click=''),
#             Button(Const('Fashion & LifeStyle'), id='b_travel_channel_ch', on_click=''),
#             Button(Const('Luxe HD'),id='b_wildlife_ch', on_click=''),
#             Button(Const('Fashion TV HD'), id='b_t24_ch', on_click=''),
#             Button(Const('Food Network'), id='b_live_planet_ch', on_click=''),
#             Button(Const('Fashion & Style 4K!'),id='b_dtx_ch', on_click=''),
#             Button(Const('Открытый мир'), id='b_travel_plus_adventure_hd_ch', on_click=''),
#             Button(Const('Global Start'), id='b_hd_media_ch', on_click=''),
#             Button(Const('НТВ Стиль'), id='b_hd_media_ch', on_click=''),
#             Button(Const('Fashion Box HD'), id='b_hd_media_ch', on_click=''),
#             Button(Const('Доктор'), id='b_hd_media_ch', on_click=''),
#             Button(Const('Дайвинг.TV'), id='b_hd_media_ch', on_click=''),
#             Button(Const('4K Fashion TV'), id='b_hd_media_ch', on_click=''),
#             Button(Const('Первый вегетарианский'), id='b_hd_media_ch', on_click=''),
#             Button(Const('Вкусное TV'), id='b_hd_media_ch', on_click=''),
#             Button(Const('Joy Cook'), id='b_hd_media_ch', on_click=''),
#             Button(Const('Бьюти.TV'), id='b_hd_media_ch', on_click=''),
#             Button(Const('Диалоги о рыбалке'), id='b_hd_media_ch', on_click=''),
#             Button(Const('Перпетуум Мобиле'), id='b_hd_media_ch', on_click=''),
#             Button(Const('Русский Экстрим'), id='b_hd_media_ch', on_click=''),
#             Button(Const('HGTV'), id='b_hd_media_ch', on_click=''),
#             id='channel_group_5',
#             width=3,
#             height=5
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=HobbieSG.start
#     ),
# )

# ############################################################################

# entertain_dialog = Dialog(
#     Window(
#         Const(text='Развлечения 👇'),
#         Row(
#             Button(Const('Мужской'), id='b_men_ch', on_click=''),
#             Button(Const('LUXURY'),id='b_luxury_ch', on_click=''),
#             Button(Const('Театр'), id='b_theatre_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Сарафан'), id='b_sarafan_ch', on_click=''),
#             Button(Const('О2ТВ'),id='b_02tv_ch', on_click=''),
#             Button(Const('Жара'), id='b_warm_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('СТС Love'), id='b_sts_love_ch', on_click=''),
#             Button(Const('E TV'),id='b_tv5_e_tv_ch', on_click=''),
#             Button(Const('Точка ТВ'), id='b_dote_tv_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('КВН ТВ'), id='b_kvn_tv_ch', on_click=''),
#             Button(Const('Анекдот ТВ'),id='b_anecdote_tv_ch', on_click=''),
#             Button(Const('HITV'), id='b_hitv_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('ТНТ HD'), id='b_tnt_hd_ch', on_click=''),
#             Button(Const('7 TV'),id='b_7tv_ch', on_click=''),
#             Button(Const('ТВТУР'), id='b_tvtour_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Мужской'), id='b_men_ch', on_click=''),
#             Button(Const('Народ Все Видит'),id='b_people_sees_everything_ch', on_click=''),
#             Button(Const('Новый Игровой Канал'), id='b_new_game_channel_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Epic'), id='b_epic_ch', on_click=''),
#             Button(Const('Мы'), id='b_we_ch', on_click=''),
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=EntertainSG.start
#     ),
# )

# ##############################################################################

# hd_dialog = Dialog(
#     Window(
#         Const(text='HD 👇'),
#         ScrollingGroup(
#             Button(Const('Кинопоказ HD'), id='b_kinopokaz_ch', on_click=''),
#             Button(Const('1 HD Music Television'),id='b_hd_music_television_ch', on_click=''),
#             Button(Const('KHL Prime'), id='b_khl_prime_ch', on_click=''),
#             Button(Const('Travel+ Adventure HD'), id='b_travelplus_adventure_hd_ch', on_click=''),
#             Button(Const('Матч! Футбол 2 HD'),id='b_match_football2_hd_ch', on_click=''),
#             Button(Const('Матч! Футбол 1 HD'), id='b_match_football1_hd_ch', on_click=''),
#             Button(Const('Luxe HD'), id='b_luxe_hd_ch', on_click=''),
#             Button(Const('Mezzo Live'),id='b_mezzo_live_ch', on_click=''),
#             Button(Const('HD Медиа'), id='b_hd_media_ch', on_click=''),
#             Button(Const('National Geographic HD'), id='b_national_geographic_hd_ch', on_click=''),
#             Button(Const('Приключения HD'),id='b_adventure_hd_ch', on_click=''),
#             Button(Const('HDL'), id='b_hdl_ch', on_click=''),
#             Button(Const('Первый HD'), id='b_first_hd_ch', on_click=''),
#             Button(Const('Animal Planet HD'),id='b_animal_planet_hd_ch', on_click=''),
#             Button(Const('Киносемья'), id='b_kinofamily_ch', on_click=''),
#             Button(Const('Россия 1 HDРоссия 1 HD'), id='b_russia1_hd_ch', on_click=''),
#             Button(Const('Fashion TV HD'),id='b_fashion_tv_hd_ch', on_click=''),
#             Button(Const('National Geographic Wild HD'), id='b_national_geographic_wild_hd_ch', on_click=''),
#             Button(Const('Fox Life HD'), id='b_fox_life_hd_ch', on_click=''),
#             Button(Const('MTV Live International HD'),id='b_mtv_international_hd_ch', on_click=''),
#             Button(Const('Travel Channel HD'), id='b_travel_channel_hd_ch', on_click=''),
#             Button(Const('Страшное HD'), id='b_scary_hd_ch', on_click=''),
#             Button(Const('Discovery Channel HD'),id='b_discovery_channel_hd_ch', on_click=''),
#             Button(Const('Капитан Фантастика'), id='b_captain_fantastic_hd_ch', on_click=''),
#             Button(Const('Insight Ultra HD'), id='b_insight_ultra_hd_ch', on_click=''),
#             Button(Const('Fuel TV HD'),id='b_fuel_tv_hd_ch', on_click=''),
#             Button(Const('Museum TV'), id='b_museum_tv_ch', on_click=''),
#             Button(Const('Охотник и Рыболов HD'), id='b_hunter_fishman_hd_ch', on_click=''),
#             Button(Const('В мире животных'),id='b_in_animal_world_hd_ch', on_click=''),
#             Button(Const('DocuBox HD'), id='b_docubox_hd_ch', on_click=''),
#             Button(Const('FilmBox HD'), id='b_filmbox_hd_ch', on_click=''),
#             Button(Const('Russian Extreme Ultra HD'), id='b_russian_extreme_ultra_hd_ch', on_click=''),
#             Button(Const('Мужское кино HD'), id='b_men_kino_hd_ch', on_click=''),
#             Button(Const('ТНТ HD'), id='b_tnt_hd_ch', on_click=''),
#             Button(Const('Fashion Box HD'), id='b_fashion_box_hd_ch', on_click=''),
#             Button(Const('Fast & Fun Box HD'), id='b_fast_fun_box_hd_ch', on_click=''),
#             Button(Const('Russian Travel Guide HD'), id='b_russian_travel_guide_hd_ch', on_click=''),
#             Button(Const('viju+ Planet'), id='b_viju_planet_hd_ch', on_click=''),
#             Button(Const('КиноМеню HD'), id='b_kinomenu_hd_ch', on_click=''),
#             Button(Const('СТС Kids HD'), id='b_sts_kids_hd_ch', on_click=''),
#             Button(Const('Блокбастер HD'), id='b_blockbaster_hd_ch', on_click=''),
#             Button(Const('Советская киноклассика HD'), id='b_soviet_kinoclassic_hd_ch', on_click=''),
#             Button(Const('Романтичное HD'), id='b_romantic_hd_ch', on_click=''),
#             Button(Const('Страшное HD'), id='b_scary_hd_ch', on_click=''),
#             Button(Const('Discovery Channel HD'), id='b_discovery_channel_hd_ch', on_click=''),
#             id='channel_group_6',
#             width=3,
#             height=5
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=HdSG.start
#     ),
# )

# ############################################################################

# adult_dialog = Dialog(
#     Window(
#         Const(text='18+ 👇'),
#         Row(
#             Button(Const('Candy TV HD'), id='b_candy_tv_hd_ch', on_click=''),
#             Button(Const('Русская ночь HD'),id='b_russian_night_hd_ch', on_click=''),
#             Button(Const('Hustler HD'), id='b_hustler_hd_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Шалун HD'), id='b_shalun_hd_ch', on_click=''),
#             Button(Const('Rsd Lips'),id='b_red_lips_ch', on_click=''),
#             Button(Const('Русская ночь'), id='b_russian_night_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Шалун'), id='b_shalun_ch', on_click=''),
#             Button(Const('Brazzers TV Evrope'),id='b_brazzers_tv_europe_ch', on_click=''),
#             Button(Const('Hustler TV Evrope'), id='b_hustler_tv_europe_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('PlayBoy TV'), id='b_playboy_tv_ch', on_click=''),
#             Button(Const('Blue Hustler 24'),id='b_blue_hustler24_ch', on_click=''),
#             Button(Const('Penthouse'), id='b_penthouse_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Exxxotica'), id='b_exxxotica_ch', on_click=''),
#             Button(Const('Redlight'),id='b_redlight_ch', on_click=''),
#             Button(Const('Redlight HD'), id='b_redlight_hd_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Dorcel TV'), id='b_dorcel_tv__ch', on_click=''),
#             Button(Const('Blue Hustler'),id='b_blue_hustler_ch', on_click=''),
#             Button(Const('Private Spice'), id='b_prvate_spice_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('French Lover'), id='b_french_lover_ch', on_click=''),
#             Button(Const('Erox'), id='b_erox_ch', on_click=''),
#             Button(Const('Candy TV'), id='b_candy_tv_ch', on_click=''),
#         ),
#         Row(
#             Button(Const('Barely legal'), id='b_barely_legal_ch', on_click=''),
#             Button(Const('Candy Man'),id='b_candy_man_ch', on_click=''),
#             Button(Const('Babes TV'), id='b_babes_tv_ch', on_click=''),
#         ),
#         Cancel(Const('◀️ Назад'), id='b_cancel'),
#         #getter=username_getter,
#         state=AdultSG.start
#     ),
# )

###########################################################################

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

# ########################################################################

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

# #########################################################################

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

# #######################################################################################################

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

# ######################################################################################################

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

# ####################################################################################################

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

# ####################################################################################################

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

# #####################################################################################################

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

# #######################################################################################################

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

# ######################################################################################################

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

# #####################################################################################################

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

# ######################################################################################################

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

# ######################################################################################################

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

# #######################################################################################################

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

# #####################################################################################################

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

# ######################################################################################################

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

# #####################################################################################################

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

# #####################################################################################################

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

# ##################################################################################################

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

# ####################################################################################################

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

# #####################################################################################################

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

# ##################################################################################################

# async def program_russia24_channel(dialog_manager: DialogManager, event_from_user: User, session: AsyncSession, **kwargs):
#     program_title = 'Россия 24'
#     res = await orm_get_programs(session, program_title)

#     # Если результат есть, форматируем его
#     if res:
#         res = "\n".join([f"{program.program_time.strftime('%H:%M')} - {program.program_title}" for program in res])
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

####################################################################################################

# @user_router.message(Command('start'))
# async def command_start_process(message: Message, dialog_manager: DialogManager):
#     await dialog_manager.start(state=MainMenuSG.start, mode=StartMode.RESET_STACK, data={'my_data': '123312'})

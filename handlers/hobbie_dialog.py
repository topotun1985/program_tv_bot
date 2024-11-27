from aiogram.fsm.state import State, StatesGroup
from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Start, Cancel, ScrollingGroup
from aiogram_dialog.widgets.text import Const
from config_data.tv_channel_utils import create_tv_channel_dialog


class HobbieSG(StatesGroup):
    start = State()


class ProBusinessSG(StatesGroup):
    start = State()


class FashionTvSG(StatesGroup):
    start = State()


class HunterFisher(StatesGroup):
    start = State()


class TelecafeSG(StatesGroup):
    start = State()


class UsadbaSG(StatesGroup):
    start = State()


class Psyhology21SG(StatesGroup):
    start = State()


class SuccessSG(StatesGroup):
    start = State()


class WeaponSG(StatesGroup):
    start = State()


class CountrySG(StatesGroup):
    start = State()


class TonusSG(StatesGroup):
    start = State()


class FishermanSG(StatesGroup):
    start = State()


class DriveSG(StatesGroup):
    start = State()


class HealthTvSG(StatesGroup):
    start = State()


class LiveAtSG(StatesGroup):
    start = State()


class KitchenTvSG(StatesGroup):
    start = State()


class AutoPlusSG(StatesGroup):
    start = State()


class FoodSG(StatesGroup):
    start = State()


class WorldBusinessChannelSG(StatesGroup):
    start = State()


class BeaverSG(StatesGroup):
    start = State()


class HorseWorldSG(StatesGroup):
    start = State()


class LuxeHDSG(StatesGroup):
    start = State()


class OpenWorldSG(StatesGroup):
    start = State()


class NtvStyleSG(StatesGroup):
    start = State()


class DoctorSG(StatesGroup):
    start = State()


class FirstVegSG(StatesGroup):
    start = State()


class JoyCookSG(StatesGroup):
    start = State()


class FishingDialoguesSG(StatesGroup):
    start = State()


hobbie_dialog = Dialog(
    Window(
        Const(text='🎣 <b>Каналы по интересам</b>'),
        ScrollingGroup(
            Start(Const('PRO Business'), id='b_pro_business_ch', state=ProBusinessSG.start),
            Start(Const('Fashion TV'),id='b_fashion_tv_ch', state=FashionTvSG.start),
            Start(Const('Охота и Рыбалка'), id='b_hunter_fisher_ch', state=HunterFisher.start),
            Start(Const('Телекафе'),id='b_telecafe_ch', state=TelecafeSG.start),
            Start(Const('Усадьба'), id='b_usadba_ch', state=UsadbaSG.start),
            Start(Const('Психология 21'), id='b_psyhology21_ch', state=Psyhology21SG.start),
            Start(Const('Успех'),id='b_success_ch', state=SuccessSG.start),
            Start(Const('Оружие'), id='b_weapon_ch', state=WeaponSG.start),
            Start(Const('Загородный'), id='b_country_ch', state=CountrySG.start),
            Start(Const('Тонус'), id='b_tonus_ch', state=TonusSG.start),
            Start(Const('Рыболов'), id='b_fisherman_ch', state=FishermanSG.start),
            Start(Const('Драйв'), id='b_drive_ch', state=DriveSG.start),
            Start(Const('Здоровое ТВ'), id='b_health_tv_ch', state=HealthTvSG.start),
            Start(Const('Живи!'),id='b_liveat_ch', state=LiveAtSG.start),
            Start(Const('Кухня ТВ'), id='b_kitchen_tv_ch', state=KitchenTvSG.start),
            Start(Const('Авто Плюс'), id='b_auto_plus_ch', state=AutoPlusSG.start),
            Start(Const('Еда'),id='b_food_ch', state=FoodSG.start),
            Start(Const('World Business Channel'), id='b_world_business_channel_ch', state=WorldBusinessChannelSG.start),
            Start(Const('Бобер'),id='b_beaver_ch', state=BeaverSG.start),
            Start(Const('Конный мир'), id='b_horse_world_ch', state=HorseWorldSG.start),
            Start(Const('Luxe HD'),id='b_luxe_hd_ch', state=LuxeHDSG.start),
            Start(Const('Открытый мир'), id='b_open_world_ch', state=OpenWorldSG.start),
            Start(Const('НТВ Стиль'), id='b_ntv_style_ch', state=NtvStyleSG.start),
            Start(Const('Доктор'), id='b_doctor_ch', state=DoctorSG.start),
            Start(Const('Первый вегетарианский'), id='b_first_veg_ch', state=FirstVegSG.start),
            Start(Const('JOY COOK'), id='b_joy_cook_ch', state=JoyCookSG.start),
            Start(Const('Диалоги о рыбалке'), id='b_fishing_dialogues_ch', state=FishingDialoguesSG.start),
            id='channel_group_5',
            width=3,
            height=5
        ),
        Cancel(Const('◀️ Назад'), id='b_cancel'),
        #getter=username_getter,
        state=HobbieSG.start
    ),
)


pro_business_channel = create_tv_channel_dialog('PRO Business', ProBusinessSG.start)
fashion_tv_channel = create_tv_channel_dialog('Fashion TV', FashionTvSG.start)
hunter_fisher_channel = create_tv_channel_dialog('Охота и рыбалка', HunterFisher.start)
telecafe_channel = create_tv_channel_dialog('Телекафе', TelecafeSG.start)
usadba_channel = create_tv_channel_dialog('Усадьба', UsadbaSG.start)
psyhology21_channel = create_tv_channel_dialog('Психология 21', Psyhology21SG.start)
success_channel = create_tv_channel_dialog('Успех', SuccessSG.start)
weapon_channel = create_tv_channel_dialog('Оружие', WeaponSG.start)
country_hobbie_channel = create_tv_channel_dialog('Загородный', CountrySG.start)
tonus_channel = create_tv_channel_dialog('Тонус', TonusSG.start)
fisherman_channel = create_tv_channel_dialog('Рыболов', FishermanSG.start)
drive_channel = create_tv_channel_dialog('Драйв', DriveSG.start)
health_tv_channel = create_tv_channel_dialog('Здоровое ТВ', HealthTvSG.start)
liveat_channel = create_tv_channel_dialog('ЖИВИ!', LiveAtSG.start)
kitchen_tv_channel = create_tv_channel_dialog('Кухня ТВ', KitchenTvSG.start)
auto_plus_channel = create_tv_channel_dialog('Авто Плюс', AutoPlusSG.start)
food_channel = create_tv_channel_dialog('ЕДА', FoodSG.start)
world_business_channel = create_tv_channel_dialog('World Business Channel', WorldBusinessChannelSG.start)
beaver_channel = create_tv_channel_dialog('Бобер', BeaverSG.start)
horse_world_channel = create_tv_channel_dialog('Конный мир', HorseWorldSG.start)
lux_hd_channel = create_tv_channel_dialog('Luxe HD', LuxeHDSG.start)
open_world_channel = create_tv_channel_dialog('Открытый мир', OpenWorldSG.start)
ntv_style_channel = create_tv_channel_dialog('НТВ Стиль', NtvStyleSG.start)
doctor_channel = create_tv_channel_dialog('Доктор', DoctorSG.start)
first_veg_channel = create_tv_channel_dialog('Первый вегетарианский', FirstVegSG.start)
joy_cook_channel = create_tv_channel_dialog('JOY COOK', JoyCookSG.start)
fishing_dialogues_channel = create_tv_channel_dialog('Диалоги о рыбалке', FishingDialoguesSG.start)

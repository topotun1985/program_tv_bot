from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, User, LabeledPrice, PreCheckoutQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram_dialog import Dialog, DialogManager, StartMode, Window
from aiogram_dialog.widgets.kbd import Start, Row
from aiogram_dialog.widgets.text import Const, Format
from handlers.fed_dialog import FedChanSG
from handlers.adult_dialog import AdultSG
from handlers.child_dialog import ChildSG
from handlers.educat_dialog import EduSG
from handlers.entertain_dialog import EntertainSG
from handlers.film_dialog import FilmSG
from handlers.hobbie_dialog import HobbieSG
from handlers.info_dialog import InfoSG
from handlers.music_dialog import MusicSG
from handlers.sport_dialog import SportSG
from handlers.favorites_dialog import FavoritesSG
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram_dialog import Dialog, Window, DialogManager
from database.orm_query import (
    add_new_user, ensure_user_exists,
    save_donation, get_user_total_donations
)
from aiogram.fsm.context import FSMContext  # Для работы с состояниями
from aiogram.filters.state import State, StatesGroup
from config_data.config import user
import logging


start_router = Router()


class MainMenuSG(StatesGroup):
    start = State()


class DonateStates(StatesGroup):
    waiting_for_amount = State()


async def username_getter(dialog_manager: DialogManager, event_from_user: User, **kwargs):
    # Используем first_name, если оно есть, иначе - username, если и оно отсутствует, то используем "Друг"
    return {'username': event_from_user.first_name or event_from_user.username or 'Друг'}


start_dialog = Dialog(
    Window(
        Format('<b>Привет, <b>{username}</b>!</b>\n'),
        Const('Здесь вы сможете найти программы передач 📺 на любой вкус.\n'),
        Const('Просто выберите категорию и канал, и я покажу, что сегодня идёт в эфире! 👇\n'),
        Row(
            Start(Const('Общероссийские 🇷🇺'),id='b_main_menu', state=FedChanSG.start),
            Start(Const('Фильмы и сериалы 🎬'), id='b_film', state=FilmSG.start),
        ),
        Row(
            Start(Const('Познавательные 📚'), id='b_educat', state=EduSG.start),
            Start(Const('Спортивные ⚽️'),id='b_sport', state=SportSG.start),
        ),
        Row(
            Start(Const('Детские 🧒'), id='b_children', state=ChildSG.start),
            Start(Const('Информационые 📰'), id='b_info', state=InfoSG.start),
        ),
        Row(
            Start(Const('Музыкальные 🎧'),id='b_music', state=MusicSG.start),
            Start(Const('Хобби 🎣'), id='b_hobbie', state=HobbieSG.start),
        ),
        Row(
            Start(Const('Развлекательные  🎉'), id='b_entertain', state=EntertainSG.start),
            Start(Const('Для взрослых 🔞'), id='b_adult', state=AdultSG.start),
        ),
        Start(Const('Избранные ❤️'), id='go_second', state=FavoritesSG.start),
        getter=username_getter,
        state=MainMenuSG.start
    ),
)


@start_router.message(Command('start'))
async def command_start_process(message: Message, dialog_manager: DialogManager, session: AsyncSession):
    # Создаем пользователя при первом запуске
    user_id = str(message.from_user.id)
    username = message.from_user.username or message.from_user.first_name
    await add_new_user(session, user_id, username)
    await dialog_manager.start(state=MainMenuSG.start, mode=StartMode.RESET_STACK)


@start_router.message(Command('help'))
async def process_help_command(message: Message):
    help_text = (
        "Привет! 👋 Вот список категорий, доступных в боте:\n\n"
        "🇷🇺 *Общероссийские* — основные телеканалы России.\n"
        "🎬 *Фильмы и сериалы* — только лучшие фильмы и сериалы.\n"
        "📚 *Познавательные* — каналы с научными и образовательными программами.\n"
        "⚽️ *Спортивные* — всё о спорте: футбол, хоккей, баскетбол и не только.\n"
        "🧒 *Детские* — безопасные каналы для детей.\n"
        "📰 *Информационные* — новости и актуальные события.\n"
        "🎧 *Музыкальные* — музыка на любой вкус.\n"
        "🎣 *Хобби* — каналы для увлечений, например рыбалка или кулинария.\n"
        "🎉 *Развлекательные* — каналы с шоу и комедиями.\n"
        "🔞 *Для взрослых* — каналы для старшей аудитории.\n"
        "❤️ *Избранные* — сохраните любимые каналы для быстрого доступа.\n\n"
        "Используйте команду /start, чтобы начать, или выберите категорию в меню.\n"
        "Используйте команду /donate - поддержать бота звездами\n"
        "Используйте команду /mystars - посмотреть историю ваших донатов\n"
        "Используйте команду /paysupport - информация о системе поддержки\n\n"
        "Если программа не отображается, попробуйте снова отправить команду /start, чтобы обновить меню. 😊"
    )
    await message.answer(help_text, parse_mode="Markdown")


@start_router.message(Command('support'))
async def send_feedback_info(message: Message):
    await message.answer("Если у вас есть вопросы или предложения, напишите на почту:\n📩 progtvbot@rambler.ru")


@start_router.message(Command("donate"))
async def donate_command(message: Message, state: FSMContext):
    await message.answer(
        "💫 Введите количество звезд, которое хотите отправить (от 1 до 100000):"
    )
    await state.set_state(DonateStates.waiting_for_amount)


@start_router.message(DonateStates.waiting_for_amount)
async def process_donate_amount(message: Message, state: FSMContext):
    try:
        amount = int(message.text)
        if not 1 <= amount <= 100000:
            await message.answer("❌ Количество звезд должно быть от 1 до 100000.")
            return
        
        prices = [LabeledPrice(label="XTR", amount=amount)]
        await message.answer_invoice(
            title="Поддержка Program TV Bot",
            description=f"Поддержать бота {amount} звездами",
            prices=prices,
            provider_token="",  # Для Stars оставляем пустым
            payload=f"tv_bot_support_{amount}",
            currency="XTR",
            reply_markup=InlineKeyboardBuilder().button(
                text=f"Отправить {amount} ⭐️",
                pay=True
            ).as_markup()
        )
        await state.clear()
    except ValueError:
        await message.answer("❌ Пожалуйста, введите целое число.")


@start_router.pre_checkout_query()
async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):
    try:
        await pre_checkout_query.answer(ok=True)
    except Exception as e:
        logging.error(f"Pre-checkout error: {e}")
        await pre_checkout_query.answer(
            ok=False,
            error_message="Произошла ошибка. Попробуйте позже."
        )


@start_router.message(F.successful_payment)
async def successful_payment_handler(message: Message, session: AsyncSession):
    payment_info = message.successful_payment
    
    try:
        # Сохраняем информацию о донате
        await save_donation(
            session,
            message.from_user.id,
            payment_info.total_amount,
            payment_info.telegram_payment_charge_id
        )
        
        # Получаем общую сумму донатов пользователя
        total_donated = await get_user_total_donations(session, message.from_user.id)
        
        await message.answer(
            f"🎉 Спасибо за поддержку! Вы отправили {payment_info.total_amount} звезд.\n"
            f"Всего вы поддержали бота на {total_donated} звезд!\n"
            "Ваша поддержка помогает нам развивать бота!"
        )
    except Exception as e:
        logging.error(f"Error saving donation: {e}")
        await message.answer(
            "⚠️ Платеж прошел успешно, но возникла ошибка при сохранении информации."
        )


@start_router.message(Command("mystars"))
async def my_stars_command(message: Message, session: AsyncSession):
    total_donated = await get_user_total_donations(session, message.from_user.id)
    await message.answer(
        f"🌟 Ваша поддержка:\n"
        f"Всего вы поддержали бота на {total_donated} звезд!\n"
        "Спасибо за вашу поддержку!"
    )


@start_router.message(Command("paysupport"))
async def pay_support_handler(message: Message):
    await message.answer(
        "ℹ️ Информация о поддержке бота:\n\n"
        "1. Вы можете поддержать бота звездами через команду /donate\n"
        "2. Все пожертвования добровольные\n"
        "3. Добровольные пожертвования не подразумевают возврат средств, "  
        "однако, если вы очень хотите вернуть средства - свяжитесь с нами.\n" 
        "4. По вопросам поддержки пишите: progtvbot@rambler.ru"
    )




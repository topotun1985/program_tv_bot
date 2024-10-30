import asyncio
import logging
from aiogram import Bot, Dispatcher, Router
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import CallbackQuery, Message, User
from aiogram_dialog import Dialog, DialogManager, StartMode, Window, setup_dialogs
from aiogram_dialog.widgets.kbd import Button, Row, Select, Group, Checkbox, ManagedCheckbox
from aiogram_dialog.widgets.text import Const, Format, List, Multi
from config_data.config import Config, load_config
from config_data.tv_program_config import CHANNEL_GROUPS
from middlewars.db import DataBaseSession
from database.engine import create_db, drop_db, session_maker


# Инициализируем логгер
logger = logging.getLogger(__name__)


async def on_startup(bot):
    run_param = False
    if run_param:
        await drop_db()
    await create_db()


async def on_shutdown(bot):
    print('бот лег!!!')

# Функция конфигурирования и запуска бота
async def main():
    # Конфигурируем логирование
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')

    # Выводим в консоль информацию о начале запуска бота
    logger.info('Starting bot')

    # Загружаем конфиг в переменную config
    config: Config = load_config()

    # Инициализируем объект хранилища
    # storage = ...

    # Инициализируем бот и диспетчер
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher()

    # Инициализируем другие объекты (пул соединений с БД, кеш и т.п.)
    # ...
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    # Помещаем нужные объекты в workflow_data диспетчера
    # dp.workflow_data.update(...)

    # Настраиваем главное меню бота

    # Регистриуем роутеры
    logger.info('Подключаем роутеры')

    for group in CHANNEL_GROUPS.values():
        dp.include_routers(*group)

    setup_dialogs(dp)

    # Регистрируем миддлвари
    logger.info('Подключаем миддлвари')
    # ...

    # Пропускаем накопившиеся апдейты и запускаем polling
    # await create_db()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


asyncio.run(main())

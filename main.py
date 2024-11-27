import asyncio
import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram_dialog import setup_dialogs
from config_data.config import Config, load_config
from config_data.tv_program_config import CHANNEL_GROUPS
from middlewars.db import DataBaseSession
from middlewars.error_handler import ErrorHandlerMiddleware
from database.engine import create_db, drop_db, session_maker
from tasks.scheduler import configure_scheduler
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder
from redis.asyncio import Redis



# Инициализируем логгер
logger = logging.getLogger(__name__)


async def on_startup(bot: Bot):
    run_param = False
    if run_param:
        await drop_db()
    await create_db()
    logger.info("Бот запущен")


async def on_shutdown(bot: Bot):
    # Закрытие сессии при завершении работы
    await bot.session.close()
    print("Бот завершил работу")


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

    redis_url = f"redis://{os.getenv('REDIS_HOST', '172.18.0.3')}:6379"
    redis = Redis.from_url(redis_url, decode_responses=True)
    try:
        await redis.ping()
        logger.info("Successfully connected to Redis")
    except Exception as e:
        logger.error(f"Failed to connect to Redis: {e}")
        raise
    
    # Создаем storage для состояний
    storage = RedisStorage(
        redis=redis,
        key_builder=DefaultKeyBuilder(
            with_bot_id=True,
            with_destiny=True
        )
    )

    # Инициализируем бот и диспетчер
    bot = Bot(
        token=config.tg_bot.token,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )
    dp = Dispatcher(storage=storage)

    # Инициализируем другие объекты (пул соединений с БД, кеш и т.п.)
    session = session_maker()
    configure_scheduler(session)

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))
    dp.update.middleware(ErrorHandlerMiddleware())

    # Регистриуем роутеры
    logger.info('Подключаем роутеры')

    for group in CHANNEL_GROUPS.values():
        dp.include_routers(*group)

    setup_dialogs(dp)

    # Регистрируем миддлвари
    logger.info('Подключаем миддлвари')

    # Пропускаем накопившиеся апдейты и запускаем polling
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()
        await redis.close()

if __name__ == '__main__':
    asyncio.run(main())

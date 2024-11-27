import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from sqlalchemy.ext.asyncio import AsyncSession
from selenium_parse.func_parse_tv import load_channel_config, parse_all_channels_sync
from database.orm_query import add_channel_program, orm_delete_all_programs


logger = logging.getLogger(__name__)


# Функция для добавления программ
async def scheduled_add_channel_program(session: AsyncSession):
    try:
        channels = load_channel_config('config_data/channels_config.json')
        channel_programs = parse_all_channels_sync(channels)
        for channel_name, program_data in channel_programs:
            await add_channel_program(session, channel_name, program_data)
        logger.info("Программы всех каналов успешно добавлены!")
    except Exception as e:
        logger.error(f'Ошибка при добавлении программ: {str(e)}')


# Функция для удаления программ
async def scheduled_delete_channel_program(session: AsyncSession):
    try:
        await orm_delete_all_programs(session)
        logger.info("Все программы успешно удалены!")
    except Exception as e:
        logger.error(f'Ошибка при удалении программ: {str(e)}')


# Функция для настройки планировщика
def configure_scheduler(session: AsyncSession):
    scheduler = AsyncIOScheduler()

    # Задачи на 05:00
    scheduler.add_job(
        scheduled_delete_channel_program,
        trigger=CronTrigger(hour=5, minute=10),
        args=[session]
    )
    scheduler.add_job(
        scheduled_add_channel_program,
        trigger=CronTrigger(hour=5, minute=10, second=20),  # Выполнить после удаления
        args=[session]
    )

    scheduler.start()
    logger.info("Планировщик задач запущен.")
    return scheduler

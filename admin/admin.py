import logging
from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession
from selenium_parse.func_parse_tv import load_channel_config, parse_all_channels_sync
from database.orm_query import (
        add_channel_program,
        orm_delete_all_programs
    )
from sqlalchemy import select, insert, values, update, delete, func, and_, or_


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

admin_router = Router()

# @admin_router.message(Command('addchannelprogramm'))
# async def process_add_channel_programm(message: Message, session: AsyncSession):
#     try:
#         # Загружаем конфигурацию каналов
#         channels = load_channel_config('config_data/channels_config.json')

#         # Парсинг всех каналов синхронно
#         channel_programs = parse_all_channels_sync(channels)

#         # Добавляем программы в БД для каждого канала
#         for channel_name, program_data in channel_programs:
#             await add_channel_program(session, channel_name, program_data)

#         # Отправляем сообщение о завершении операции
#         await message.answer('Программы всех каналов добавлены!', parse_mode=None)

#     except Exception as e:
#         await message.answer(f'Ошибка: \n{str(e)}\nОбратитесь в поддержку', parse_mode=None)



# @admin_router.message(Command('deletechannelprogramm'))
# async def process_delete_channel_programm(message: Message, session: AsyncSession):
#     try:
#         # Вызываем функцию для удаления всех программ
#         await orm_delete_all_programs(session)
#         await message.answer("Все программы успешно удалены!", parse_mode=None)
#     except Exception as e:
#         await message.answer(f"Ошибка: \n{str(e)}\nОбратитесь в поддержку", parse_mode=None)

# =================================================================================

# @admin_router.message(Command('addprogram'))
# async def process_admin_command(message: Message, session: AsyncSession):
#     try:
#         await orm_add_program(session)
#         await message.answer('Данные добавлены!')
#     except Exception as e:
#         await message.answer(
#             f' Ошибка: \n{str(e)}\nОбратитесь в поддержку'
#         )

# @admin_router.message(Command('addfirstchannelprogramm'))
# async def process_add_programm_first_channel(message: Message, session: AsyncSession):
#     try:
#         await add_russia_one_channel_program(session)
#         # Отключаем разметку, если она не нужна
#         await message.answer('Данные добавлены!', parse_mode=None)
#     except Exception as e:
#         # Здесь также отключаем разметку, если ошибка может содержать спецсимволы
#         await message.answer(
#             f'Ошибка: \n{str(e)}\nОбратитесь в поддержку', parse_mode=None
#         )


# @admin_router.message(Command('addchannelprogramm'))
# async def process_add_channel_programm(message: Message, session: AsyncSession):
#     try:
#         # Загружаем конфигурацию всех каналов из JSON
#         channels = load_channel_config('config_data/channels_config.json')

#         # Итерируемся по каждому каналу в конфигурации
#         for channel in channels:
#             channel_name = channel["name"]
#             channel_url = channel["url"]
#             time_class = channel["time_class"]
#             title_class = channel["title_class"]

#             # Парсим программы канала
#             program_data = parse_channel(channel_url, time_class, title_class)

#             # Добавляем данные в БД для каждого канала
#             await add_channel_program(session, channel_name, program_data)

#         # Отправляем сообщение о завершении операции
#         await message.answer('Программы всех каналов добавлены!', parse_mode=None)

#     except Exception as e:
#         await message.answer(f'Ошибка: \n{str(e)}\nОбратитесь в поддержку', parse_mode=None)

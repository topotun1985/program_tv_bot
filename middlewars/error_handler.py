from typing import Any, Callable, Dict, Awaitable
from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, CallbackQuery, Message
from aiogram_dialog.api.exceptions import UnknownIntent
import logging

logger = logging.getLogger(__name__)

class ErrorHandlerMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        try:
            return await handler(event, data)
        except UnknownIntent:
            # Обработка ошибки устаревшей кнопки
            if isinstance(event, CallbackQuery):
                user_id = event.from_user.id
                logger.warning(f"UnknownIntent для пользователя {user_id}")
                await event.message.answer(
                    "🔄 Извините, но эта кнопка больше не активна.\n"
                    "Пожалуйста, используйте команду /start, "
                    "чтобы начать диалог заново."
                )
                await event.answer()
            return True
        except Exception as e:
            # Общая обработка ошибок
            error_msg = f"Ошибка: {type(e).__name__}: {str(e)}"
            logger.error(error_msg, exc_info=True)
            
            # Определяем пользователя для логирования
            user_id = None
            if isinstance(event, CallbackQuery):
                user_id = event.from_user.id
                await event.message.answer(
                    "❌ Произошла ошибка при обработке запроса.\n"
                    "Пожалуйста, попробуйтеи использовать команду /start"
                )
                await event.answer()
            elif isinstance(event, Message):
                user_id = event.from_user.id
                await event.answer(
                    "❌ Произошла ошибка при обработке сообщения.\n"
                    "Пожалуйста, попробуйтеи использовать команду /start"
                )
            
            if user_id:
                logger.error(f"Ошибка для пользователя {user_id}: {error_msg}")
            return True

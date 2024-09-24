import asyncio

from src.configs.logger_setup import logger
from src.presentation.rest.bot import bot, dp



async def start_bot():
    logger.info("Бот Запущен!!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(start_bot())

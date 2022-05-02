import asyncio
from loguru import logger

from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import get_config


async def main() -> None:
    """Run bot"""
    config = get_config()
    logger.add(sink='logs.log', format='{time}|{level}|{message}')

    bot = Bot(token=config.telegram.bot_token, parse_mode=ParseMode.HTML)
    dp = Dispatcher(bot=bot, storage=MemoryStorage())

    try:
        logger.info('Bot run polling')
        await dp.start_polling()
    finally:
        logger.info('Bot stop polling')
        await dp.storage.close()
        await dp.storage.wait_closed()


if __name__ == '__main__':
    asyncio.run(main=main())

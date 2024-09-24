from aiogram import Dispatcher, Bot, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from src.configs.config import settings
from src.domain.bot_service.service import WikiBotService
from src.domain.bot_service.models import FSMAdmin


bot = Bot(token=settings.BOT_TOKEN)
dp = Dispatcher()

bot_service = WikiBotService(bot, dp)

@dp.message(CommandStart())
async def start_bot(message: Message, state: FSMContext) -> None:
	await bot_service.start_command(message, state)


@dp.message(FSMAdmin.wiki_lang, F.text)
async def get_wiki_lang(message: Message, state: FSMContext) -> None:
	await bot_service.get_wiki_lang_service(message, state)





from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.types import ReplyKeyboardRemove

from src.configs.logger_setup import logger
from src.domain.bot_service.functions import WikiBotFunctions

from src.domain.bot_service.buttons import choice_language
from src.domain.bot_service.models import FSMAdmin


class WikiBotService(WikiBotFunctions):

	def __init__(self, bot: Bot, dp: Dispatcher) -> None:
		super().__init__()
		self.bot = bot
		self.dp = dp


	@staticmethod
	async def start_command(message: Message, state: FSMContext) -> None:
		logger.info("Бот стартанул!")
		current_state = await state.get_state()

		if current_state is not None:
			await state.clear()

		await message.answer(f"Assalomu Aleykum {message.from_user.first_name} Wikipedia botga🤖 Xush kelibsiz",)
		await message.answer(
			"Wikipediadan keladigan ma'lumot qaysi tilda bo'lishini xoxlaysiz: ",
			reply_markup=choice_language, parse_mode=ParseMode.MARKDOWN
		)

		await state.set_state(FSMAdmin.wiki_lang)


	@staticmethod
	async def get_wiki_lang_service(message: Message, state: FSMContext) -> None:
		wiki_languages = {"O'zbek Tili🇺🇿": "uz", "Русский🇷🇺": "ru", "English🇺🇸": "en"}

		language = wiki_languages.get(message.text)

		if language:
			await message.answer(f"{message.text} tili tanlandi\n\n"
			                     f"Agar tilni o'zgartirmoqchi bo'lsangiz Меню bo'limidan set_lang bo'limini tanlang")

			logger.info(f"{message.text} tili tanlandi")
			await message.answer(
				"Endi menga har qanday so'zni yuboring va men uning ma'nosini Wikipediada🌐 topaman",
				reply_markup=ReplyKeyboardRemove()
			)

			await state.update_data(wiki_lang=language)

			await state.set_state(FSMAdmin.text)

		else:
			await message.answer("Ko'rsatilgan tildan birini tanlang!")



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
		wiki_languages = {"O'zbek🇺🇿": "uz", "Русский🇷🇺": "ru", "English🇺🇸": "en"}

		language = wiki_languages.get(message.text)

		if language:
			await message.answer(f"{message.text} tili tanlandi\n\n"
			                     f"Agar tilni o'zgartirmoqchi bo'lsangiz Меню bo'limidan change_language bo'limini tanlang")

			logger.info(f"{message.text} tili tanlandi")
			await message.answer(
				"Endi menga har qanday so'zni yuboring va men uning ma'nosini Wikipediada🌐 topaman",
				reply_markup=ReplyKeyboardRemove()
			)

			await state.update_data(wiki_lang=language)

			await state.set_state(FSMAdmin.text)

		else:
			await message.answer("Ko'rsatilgan tildan birini tanlang!")


	@staticmethod
	async def change_language_service(message: Message, state: FSMContext) -> None:
		await state.set_state(FSMAdmin.wiki_lang)
		await message.answer("Tilni tanlang: ", reply_markup=choice_language)


	@staticmethod
	async def bot_help_command(message: Message) -> None:
		await message.answer(
			"Salom 👋! Bu Wikipedia bot. Bu yerda siz har qanday mavzu bo'yicha ma'lumot 📕 olishingiz mumkin.\n"
			"Shunchaki menga istalgan so'zni yuboring va men uni Wikipediadan 🌐 topib beraman.\n\n"
			"Agar Wikipediadan keladigan ma'lumotlar tilini o'zgartirmoqchi bo'lsangiz,\n"
			"iltimos, Menyu bo'limidan **change_language** bo'limini tanlang."
		)



	async def send_info_service(self, message: Message, state: FSMContext) -> None:

		state_data = await state.get_data()
		wiki_language = state_data.get('wiki_lang')

		information_about_something = await self.get_wiki(message.text, wiki_language)

		if information_about_something:
			await message.answer(information_about_something, parse_mode=ParseMode.MARKDOWN)

		else:
			await message.answer("🔍 Wikipediada bu haqida ma'lumot yo'q🤷!")

		await state.set_state(FSMAdmin.text)



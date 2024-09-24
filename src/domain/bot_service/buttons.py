from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


choice_language = ReplyKeyboardMarkup(
	keyboard=[
		[KeyboardButton(text="O'zbek Tili🇺🇿")],
		[KeyboardButton(text="Русский🇷🇺")],
	    [KeyboardButton(text="English🇺🇸")]
	],
	resize_keyboard=True
)



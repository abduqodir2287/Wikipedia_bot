from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

uz = KeyboardButton("Uzbek tili")
ru = KeyboardButton("Rus tili")
en = KeyboardButton("Ingliz tili")

keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(uz).add(ru, en)


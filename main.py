from aiogram import Bot, Dispatcher, types, executor
import wikipedia
import re
import logging
from wiki_bot_class import Wiki_helperDB
from config import wiki_bot_token
from buttons import keyboard_markup

bot = Bot(token=wiki_bot_token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

base = Wiki_helperDB("Wiki.db")

wikipedia.set_lang("uz")
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not('==' in x):
                if len((x.strip())) > 3:
                    wikitext2 = wikitext2+x+'.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub("\{[^\{\}]*\}", '', wikitext2)
        return f"Barcha malumotlar👇👇\n" \
               f"\n" \
               f"{wikitext2}\n" \
               f"\n" \
               f"Boshqa narsalar xaqida xam bilishni xoxlasangiz🙋‍♂️\n" \
               f"Har qanday so'zni yuboring✍️"
    except Exception:
        return "Wikipediada bu xaqida ma'lumot yo'q🤷!"

@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer("Assalomu Aleykum Wikipedia botga🤖 Xush kelibsiz")
    await message.answer("Tilni tanlang:   ", reply_markup=keyboard_markup)
    base.add_item(message.from_user.id, message.from_user.username)

@dp.message_handler(content_types="text")
async def handle_text(message: types.Message):
    lang = None
    if message.text == "Uzbek tili":
        lang = 'uz'
    elif message.text == "Rus tili":
        lang = 'ru'
    elif message.text == "Ingliz tili":
        lang = 'en'

    if lang:
        wikipedia.set_lang(lang)
        await message.reply("Til muvaffaqiyatli o'zgartirildi!")
        await message.answer("Menga har qanday so'zni yuboring va men uning ma'nosini Wikipediada🌐 topaman")
    else:
        await message.reply(f"{getwiki(message.text)}")


async def startup(dp: Dispatcher):
    base.setup('Wiki')
    print('Bot ishga tushdi ')

async def shutdown(dp: Dispatcher):
    print("Good bye!")
    base.log_out()

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=startup, on_shutdown=shutdown, skip_updates=True)

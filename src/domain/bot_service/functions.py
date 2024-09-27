import wikipedia
import re

from src.configs.logger_setup import logger


class WikiBotFunctions:

	@staticmethod
	async def get_wiki(text: str, wiki_language: str) -> str | bool:
		try:
			wikipedia.set_lang(wiki_language)

			page = wikipedia.page(text)

			wikitext = page.content[:1000]

			sentences = wikitext.split('.')

			sentences = sentences[:-1]

			clean_text = ''
			for sentence in sentences:
				if '==' not in sentence and len(sentence.strip()) > 3:
					clean_text += sentence.strip() + '. '

			clean_text = re.sub(r'\([^()]*\)', '', clean_text)
			clean_text = re.sub('\\{[^\\{\\}]*\\}', '', clean_text)

			return (
				"🌐 Barcha ma'lumotlar👇👇\n\n"
				f"{clean_text.strip()}\n\n"
				"📚 Boshqa narsalar haqida bilishni xohlasangiz🙋‍♂️\n"
				"Har qanday so'zni yuboring✍️\n"
				"[Wikipedia](https://t.me/Wiki_in_Uzbek_language_bot) 🔝\n"
			)

		except Exception as e:
			logger.warning(f"{e}")
			return False



from aiogram.fsm.state import State, StatesGroup


class FSMAdmin(StatesGroup):
	wiki_lang = State()
	text = State()



from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


class Form(StatesGroup):
    account_activity: list[bool, bool] = [False, False]
    admin_state: int = 4
    user_id: int = 0
    bot_registering: State = State()
    admin = State()
    translator = State()
    delete = State()
    new_translator_registering: State = State()

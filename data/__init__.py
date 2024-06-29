from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dataclasses import dataclass


class Form(StatesGroup):
    bot_registering = State()
    edit = State()
    admin = State()
    translator = State()
    delete = State()
    new_translator_registering = State()


@dataclass
class Info:
    user_id: str
    girl_names: list[str]
    month_balances: list[float]
    day_balances: list[float]
    account_activity: list[bool]
    admin_menu: int

    def __init__(self):
        self.girl_names = ['None', 'None']
        self.month_balances = [0.0, 0.0]
        self.day_balances = [0.0, 0.0]
        self.account_activity = [False, False]
        self.admin_menu = 4


info = Info()

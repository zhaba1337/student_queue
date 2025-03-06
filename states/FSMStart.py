from aiogram.fsm.state import State, StatesGroup

class FSMStart(StatesGroup):
    telegram_id: int = State()
    family: str = State()
    name: str = State()
    patronymic: str = State()
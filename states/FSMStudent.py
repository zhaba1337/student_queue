from aiogram.fsm.state import State, StatesGroup

class FSMStudent(StatesGroup):
    id: int = State()
    group: int = State()
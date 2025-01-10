from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext


from sqlalchemy.ext.asyncio import AsyncSession



from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove
from database.engine import Engine

router = Router()

en = Engine()

@router.message(F.text)
async def show_all_events(message: types.Message):
    await message.answer(message)


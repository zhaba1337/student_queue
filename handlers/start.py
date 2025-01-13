from aiogram import Router, F
from aiogram.filters import Command
from aiogram import types
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext

from sqlalchemy import select, insert, create_engine
from sqlalchemy.ext.asyncio import AsyncSession



from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove


from datetime import datetime


user_private_router = Router()

    
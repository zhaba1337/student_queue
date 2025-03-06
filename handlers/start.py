from aiogram import Router, F
from aiogram.filters import Command, CommandStart
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardRemove

from datetime import datetime
from typing import Dict, AnyStr, Tuple, List

from models.User import User
from models.Student import Student
from models.Group import Group
from models.CourseGroup import CourseGroup
from models.Course import Course

from database.UserQuery import UserQuery
from database.StudentQuery import StudentQuery
from database.GroupQuery import GroupQuery
from database.CourseGroupQuery import CourseGroupQuery

from states.FSMStart import FSMStart
from states.FSMStudent import FSMStudent

from kbds.inline import get_callback_btns

from callback.CBAllRight import CBAllRight
from callback.CBGroup import CBGroup
from callback.CBIncorrect import CBIncorrect

start_router = Router()


@start_router.message(CommandStart())
async def start(message: types.Message, state: FSMContext):
    await state.set_state(FSMStart.family)
    await state.update_data(telegram_id = message.chat.id)
    await message.answer('Введите фамилию')
    
@start_router.message(FSMStart.family)
async def input_family(message: types.Message, state: FSMContext):
    await state.update_data(family = message.text)
    await state.set_state(FSMStart.name)
    await message.answer("Хорошо, дальше, введите имя")
    
@start_router.message(FSMStart.name)
async def input_name(message: types.Message, state: FSMContext):
    await state.update_data(name = message.text)
    await state.set_state(FSMStart.patronymic)
    await message.answer("Дальше, введите отчество")
    
    
@start_router.message(FSMStart.patronymic)
async def input_name(message: types.Message, state: FSMContext):
    await state.update_data(patronymic = message.text)
    data = await state.get_data()
    usr_id: int = await UserQuery().Add(User(**data))
    await state.clear()
    print(data)
    await message.answer(f"Проверьте данные: {data}", reply_markup=get_callback_btns(btns={"Все верно" : CBAllRight(id = usr_id).pack(), "Ввести заново" : CBIncorrect(id = usr_id).pack()}))
   
    
@start_router.callback_query(CBIncorrect.filter())
async def incorrect_input_data(callback: types.CallbackQuery, callback_data : CBIncorrect):
    await callback.message.answer("qw")
    await UserQuery().Delete(callback_data.id)
    await start(callback.message, FSMContext) # по факту костыль потому что tg API не позволяет делать callback размером больше 64 байт
    

@start_router.callback_query(CBAllRight.filter())
async def allright_insert_db(callback: types.CallbackQuery, callback_data : CBAllRight):

    
    # all_groups = await GroupQuery().GetAll()
    # print(*all_groups)
    # btns = {group.title : CBGroup(id = callback_data.id, group_id = group.id).pack() for group in all_groups}
    
    await callback.answer()
    await callback.message.edit_text("Хорошо, дальше необходимо выбрать группу, для этого воспользуйтесь командой /group.")
    
    

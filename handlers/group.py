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

group_router = Router()

@group_router.message(Command('group'))
async def start(message: types.Message) -> None:
    all_groups = await GroupQuery().GetAll()
    print(*all_groups)
    user: User | None = await UserQuery().Get(message.chat.id)
    if user:
        btns = {group.title : CBGroup(id = user.id, group_id = group.id).pack() for group in all_groups}
        await message.answer('Ваша группа:', reply_markup=get_callback_btns(btns=btns, sizes=(len(btns), 1)))
    else:
        print('[ERROR]user not found!')
    
    
    
@group_router.callback_query(CBGroup.filter())
async def choice_group(callback: types.CallbackQuery, callback_data: CBGroup) -> None:
    await callback.answer(f'{callback_data.group_id}')
    await StudentQuery().Add(Student(**dict(callback_data)))
    await callback.message.edit_text("Хорошо, список направлений и лабораторных по ним вы сможете увидеть командой /course:")


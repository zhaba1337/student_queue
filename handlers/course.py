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
from models.Lab import Lab

from database.UserQuery import UserQuery
from database.StudentQuery import StudentQuery
from database.GroupQuery import GroupQuery
from database.CourseGroupQuery import CourseGroupQuery
from database.LabQuery import LabQuery

from states.FSMStart import FSMStart
from states.FSMStudent import FSMStudent

from kbds.inline import get_callback_btns

from callback.CBAllRight import CBAllRight
from callback.CBGroup import CBGroup
from callback.CBGetLabs import CBGetLabs
from callback.CBPassLab import CBPassLab


course_router = Router()


@course_router.message(Command('course'))
async def start(message: types.Message) -> None:
    user: User = await UserQuery().Get(message.chat.id)
    print(user)
    group_id: int = await StudentQuery().GetGroupId(user.id)
    print(group_id)
    courses: List[Course] = await CourseGroupQuery().GetCourses(group_id)
    print(*courses)
    print(courses[0].teacher.user)
    for course in courses: 
        text = f"Дисциплина: {course.title}\nПреподаватель: {course.teacher.user.fullname()}"
        callback_data = CBGetLabs(course_id=course.id, user_id = user.id).pack()
        await message.answer(text, reply_markup=get_callback_btns(btns={"Посмотреть лабы" : callback_data}))


@course_router.callback_query(CBGetLabs.filter())
async def get_labs(callback: types.CallbackQuery, callback_data : CBGetLabs) -> None:
    labs: List[Lab] = await LabQuery().Get(course_id = callback_data.course_id)
    print(*labs)
    for lab in labs:
        text = f"{lab.title}\n{lab.description}"
        btn = get_callback_btns(btns = {"Сдать лабу" : CBPassLab(lab_id = lab.id, user_id=callback_data.user_id).pack()})
        await callback.message.answer(text, reply_markup=btn)
    await callback.answer() 
    
    

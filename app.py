from aiogram import Bot, Dispatcher, types
import asyncio 
from dotenv import load_dotenv, dotenv_values
from collections import OrderedDict
from datetime import datetime

from kbds.inline import get_callback_btns
from sqlalchemy import func, DateTime

from handlers import test, start, group, course
from callback.CBPassLab import CBPassLab
from callback.CBPassed import CBPassed
from callback.CBUnpassed import CBUnpassed
from callback.CBReject import CBReject

from database.LabQuery import LabQuery
from database.CourseQuery import CourseQuery
from database.UserQuery import UserQuery
from database.StudentQueueQuery import StudentQueueQuery

from models.Lab import Lab
from models.Course import Course
from models.User import User
from models.StudentQueue import StudentQueue

import logging 



if not(load_dotenv()):
    raise (Exception("env empty, pls create .env file and add inside variables: 'TOKEN', 'DB_URL', 'DB_MIGRATION_URL'"))

config: OrderedDict = dotenv_values()
logging.basicConfig(level=logging.INFO, filename='log.log', filemode='w')


bot = Bot(token=config["TOKEN"])


dp = Dispatcher()#нашел фикс, просто нужно ипортировать bot и указать в списке параметров функции с аннотацией типа
@dp.callback_query(CBPassLab.filter())# callback здесь, потому-что для отправки сообщений в другие чаты необходимо использовать объект Bot а его импортировать нельзя, по крайней мере я не нашел способ это сделать (пока что).
async def pass_lab(callback: types.CallbackQuery, callback_data: CBPassLab) -> None:
    lab: Lab = await LabQuery().GetById(id = callback_data.lab_id)
    callback.answer(str(callback_data.lab_id))
    course: Course = await CourseQuery().GetById(lab.course_id)
    user: User = await UserQuery().GetById(id = callback_data.user_id)
    cooldown: int = course.cooldown_time
    print('-----------------\n', cooldown, '-----------------\n')
    student_cooldown: StudentQueue | None = await StudentQueueQuery().GetStudentCooldown(user.id)
    print(student_cooldown)
    try:
        print(student_cooldown.verdict_time.timestamp() + cooldown)
        print(datetime.now().timestamp())
    except: 
        pass


        
    queue_where_verdict_none: StudentQueue = await StudentQueueQuery().GetWithoutVerdict(user.id)
    queue_where_verdict_not_passed: StudentQueue | None = await StudentQueueQuery().GetWithVerdictNotPassed(user.id)
    
    try:
        await callback.message.answer(str(queue_where_verdict_not_passed.verdict_time))
        await callback.message.answer(str(datetime.now()))
        await callback.message.answer(str(queue_where_verdict_not_passed.verdict_time.timestamp() + cooldown < datetime.now().timestamp()))
    except: 
        pass
    
    
    
    if(queue_where_verdict_not_passed is not None):
        if(queue_where_verdict_not_passed.verdict_time.timestamp() + cooldown + 28800 > datetime.now().timestamp()):
            await callback.message.answer(f"Вы попытались сдать лабу - неудачно, подождите до окончания кулдауна.")
            await callback.answer()
            return 0
    

    
    if queue_where_verdict_none is None:
        s_q_id: int = await StudentQueueQuery().Add(StudentQueue(student_id = user.id,lab_id = lab.id))
        btns = {
            "Зачтено" : CBPassed(student_queue_id=s_q_id).pack(),
            "Незачтено" : CBUnpassed(student_queue_id=s_q_id).pack(),
            "Отклонить" : CBReject(student_queue_id=s_q_id).pack()
        }
        await bot.send_message(course.teacher.user.telegram_id, f"{user.fullname()}\n{lab.title}", reply_markup=get_callback_btns(btns=btns))
        await callback.answer()
        return 0 
    
    else:
        await callback.message.answer(f"Вы уже занимали очередь, лабораторная: \n{lab.title}, \nCдайте её для начала, или отмените.")
        await callback.answer()
        return 0
        



@dp.callback_query(CBPassed.filter())
async def passed_lab(callback: types.CallbackQuery, callback_data: CBPassed) -> None:
    await StudentQueueQuery().AddVerdict(callback_data.student_queue_id, 'passed', func.now())
    await callback.message.answer("Зачет")


@dp.callback_query(CBUnpassed.filter())
async def passed_lab(callback: types.CallbackQuery, callback_data: CBUnpassed) -> None:
    await StudentQueueQuery().AddVerdict(callback_data.student_queue_id, 'not_passed', func.now())
    await callback.answer("Незачет")
    

@dp.callback_query(CBReject.filter())
async def passed_lab(callback: types.CallbackQuery, callback_data: CBReject) -> None:
    await StudentQueueQuery().AddVerdict(callback_data.student_queue_id, 'rejected', func.now())
    await callback.answer("отказано")


dp.include_router(test.user_private_router)
dp.include_router(start.start_router)
dp.include_router(group.group_router)
dp.include_router(course.course_router)



        
async def on_startup(bot):
    print('поднял')
async def on_shutdown(bot):
    print('бот лег')
    
    
async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    await bot.delete_webhook(drop_pending_updates=True)
    
    await dp.start_polling(bot)
    


if __name__ == '__main__':
    asyncio.run(main())
from aiogram.filters.callback_data import CallbackData


class CBGetLabs(CallbackData, prefix='get_labs'):
    course_id: int
    user_id: int
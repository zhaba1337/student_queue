from aiogram.filters.callback_data import CallbackData


class CBCourse(CallbackData, prefix='group_id'):
    id: int

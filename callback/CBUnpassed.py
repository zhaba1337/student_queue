from aiogram.filters.callback_data import CallbackData


class CBUnpassed(CallbackData, prefix='unpassed'):
    student_queue_id: int
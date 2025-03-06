from aiogram.filters.callback_data import CallbackData


class CBReject(CallbackData, prefix='reject'):
    student_queue_id: int
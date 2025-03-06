from aiogram.filters.callback_data import CallbackData


class CBPassed(CallbackData, prefix='passed'):
    student_queue_id: int
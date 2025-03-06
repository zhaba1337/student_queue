from aiogram.filters.callback_data import CallbackData


class CBPassLab(CallbackData, prefix='pl'):
    lab_id: int
    user_id: int
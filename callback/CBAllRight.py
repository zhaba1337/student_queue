from aiogram.filters.callback_data import CallbackData


class CBAllRight(CallbackData, prefix=''):
    id: int
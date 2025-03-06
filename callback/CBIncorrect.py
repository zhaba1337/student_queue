from aiogram.filters.callback_data import CallbackData


class CBIncorrect(CallbackData, prefix='inccorect'):
    id: int
from aiogram.filters.callback_data import CallbackData


class CBGroup(CallbackData, prefix='group_id'):
    id: int
    group_id: int
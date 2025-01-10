from aiogram import Bot, Dispatcher, types
import asyncio 
from dotenv import load_dotenv, dotenv_values
from collections import OrderedDict

from handlers import msg

if not(load_dotenv()):
    raise (Exception("env empty, pls create .env file and add inside variables: 'TOKEN', 'DB_URL', 'DB_MIGRATION_URL'"))

config: OrderedDict = dotenv_values()

bot = Bot(token=config["TOKEN"])
#bot.my_admins_list = [539931122]

dp = Dispatcher()

dp.include_router(msg.router)


async def on_startup(bot):
    print('поднял')
async def on_shutdown(bot):
    print('бот лег')
    
    
async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    
    await bot.delete_webhook(drop_pending_updates=True)
    
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    
    
asyncio.run(main())
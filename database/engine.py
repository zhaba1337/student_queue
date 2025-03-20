import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine, AsyncEngine
from dataclasses import dataclass


from typing_extensions import Self

from dotenv import dotenv_values

import os
url=dotenv_values(".env")["DB_URL"], 
class Engine:
    def __init__(self):
        pass
    
    _engine: AsyncEngine = create_async_engine(
        url=url, 
        echo=True, 
        connect_args={"options": "-c timezone=utc"}
        )
    
    _session_maker: AsyncSession = async_sessionmaker(
        bind=_engine, 
        class_=AsyncSession, 
        expire_on_commit=False
        ).begin().async_session
    
    def session(self: Self) -> AsyncSession:
        return self._session_maker
    
    
engine = create_async_engine(url=url)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

def connection(method):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                # Явно не открываем транзакции, так как они уже есть в контексте
                return await method(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()  # Откатываем сессию при ошибке
                raise e  # Поднимаем исключение дальше
            finally:
                await session.close()  # Закрываем сессию

    return wrapper
    

# engine = create_async_engine(url="postgresql+psycopg://postgres_user:root@postgres/student_queue", echo=True, connect_args={"options": "-c timezone=utc"})
# session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


# async def create_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# async def drop_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)

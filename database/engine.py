import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine, AsyncEngine
from dataclasses import dataclass


from typing_extensions import Self

from dotenv import dotenv_values


@dataclass
class Engine:
    _engine: AsyncEngine = create_async_engine(
        url=dotenv_values(".env")["DB_URL"], 
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
    
    
    
    

# engine = create_async_engine(url="postgresql+psycopg://postgres:zhabka1337@localhost/bsu_priem_1", echo=True, connect_args={"options": "-c timezone=utc"})
# session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)


# async def create_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


# async def drop_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
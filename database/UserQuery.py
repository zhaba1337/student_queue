from typing import List, Any, Dict, Tuple
from typing_extensions import Self
from sqlalchemy import select, delete, update
from sqlalchemy.exc import PendingRollbackError, IntegrityError



import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from models.User import User
from .engine import Engine


class UserQuery(Engine):
    

    async def Add(self: Self, user: User) -> int:
        self.session().add(user)
        await self.session().commit()
        await self.session().flush()
        return user.id
        

    async def GetById(self: Self, id: int) -> User | None:
        result = await self.session().execute(select(User).where(User.id == id))
        return result.scalar_one_or_none()
    

    async def Get(self: Self, telegram_id: int) -> User | None:
        result = await self.session().execute(select(User).where(User.telegram_id == telegram_id))
        return result.scalar_one_or_none()
    
    
    async def GetAll(self: Self) -> List[User]:
        result = await self.session().execute(select(User))
        return result.scalars().all()
    
    
    async def Update(self: Self, id: int) -> None:
        pass
    
    
    async def Delete(self: Self, id: int) -> None:
        await self.session().execute(delete(User).where(User.id == id))
        await self.session().commit()
    
    
    
    
    
    
    
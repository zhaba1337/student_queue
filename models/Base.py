
from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint, select, delete, update
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from typing import List, Any
from typing_extensions import Self
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from database.engine import Engine



class Base(DeclarativeBase, Engine):
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __str__(self):
        return str(self.as_dict())
    
    async def Push(self: Self):
        self.session().add(self)
        print(self)
        await self.session().commit()
        
    async def Get(self: Self, id: int) -> Self:
        result = await self.session().execute(select(self).where(self.id == id))
        return result.scalar()
    
    
    async def GetMany(self: Self, id: int) -> List[Self]:
        result = await self.session().execute(select(self).where(self.id == id))
        return result.scalars()
    
    
    
    async def Delete(self: Self, id: int) -> None:
        await self.session().execute(delete(self).where(self.id == id))
        await self.session().commit()
        
    
    async def DeleteMany(self: Self, ids: List[int]) -> None:
        await self.session().execute(delete(self).where(self.id.in_(ids)))
        await self.session().commit()
        
    async def Update(self: Self, id:int, data: dict):
        pass
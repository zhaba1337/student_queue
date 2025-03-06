from typing import List, Any, Dict, Tuple
from typing_extensions import Self
from sqlalchemy import select, delete, update
from sqlalchemy.exc import PendingRollbackError, IntegrityError



import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from models.Group import Group
from .engine import Engine



class GroupQuery(Engine):
    async def Add(self: Self, group: Group) -> None:
        self.session().add(Group)
        await self.session().commit()
        
        
    async def Get(self: Self, title: str) -> Group | None:
        result = await self.session().execute(select(Group).where(Group.title.like(title)))
        return result.scalar_one_or_none()
    
    
    async def GetAll(self: Self) -> List[Group]:
        result = await self.session().execute(select(Group))
        return result.scalars().all()
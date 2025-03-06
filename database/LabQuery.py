from typing import List, Any, Dict, Tuple
from typing_extensions import Self
from sqlalchemy import select, delete, update
from sqlalchemy.exc import PendingRollbackError, IntegrityError



import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from models.Lab import Lab
from .engine import Engine



class LabQuery(Engine):        
    async def Get(self: Self, course_id: int) -> List[Lab]:
        result = await self.session().execute(select(Lab).where(Lab.course_id == course_id))
        return result.scalars().all()
    
    async def GetById(self: Self, id: int) -> Lab | None:
        result = await self.session().execute(select(Lab).where(Lab.id == id))
        return result.scalar_one_or_none()

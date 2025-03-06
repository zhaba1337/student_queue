from typing import List, Any, Dict, Tuple
from typing_extensions import Self
from sqlalchemy import select, delete, update
from sqlalchemy.exc import PendingRollbackError, IntegrityError



import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from models.Student import Student
from .engine import Engine



class StudentQuery(Engine):
    async def Add(self: Self, student: Student) -> None:
        self.session().add(student)
        await self.session().commit()
        
        
    async def GetGroupId(self: Self, id: int) -> int | None:
        result = await self.session().execute(select(Student).where(Student.id == id))
        return result.scalar().group_id

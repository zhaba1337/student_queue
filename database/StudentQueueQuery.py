from typing import List, Any, Dict, Tuple
from typing_extensions import Self
from sqlalchemy import select, delete, update, func
from sqlalchemy.exc import PendingRollbackError, IntegrityError



import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from models.StudentQueue import StudentQueue
from .engine import Engine

class StudentQueueQuery(Engine):
    async def Add(self: Self, student_queue: StudentQueue) -> int:
        self.session().add(student_queue)
        await self.session().commit()
        await self.session().flush()
        return student_queue.id
    
    async def AddVerdict(self: Self, id: int, verdict: str, verdict_time: float) -> None:
        await self.session().execute(update(StudentQueue).where(StudentQueue.id == id).values(verdict = verdict, verdict_time = verdict_time))
        await self.session().commit()
        
    async def GetById(self: Self, id: int) -> StudentQueue | None:
        result = await self.session().execute(select(StudentQueue).where(StudentQueue.id == id))
        return result.scalar_one_or_none()
    
    async def GetWithoutVerdict(self: Self, student_id: int) -> StudentQueue | None:
        #result = await self.session().execute(select(StudentQueue).where().where())
        result = await self.session().execute(select(StudentQueue).filter(StudentQueue.student_id == student_id, StudentQueue.verdict == None))
        return result.scalar_one_or_none()
    
    async def GetStudentCooldown(self: Self, student_id: int) -> StudentQueue | None:
        result = await self.session().execute(select(StudentQueue).where(StudentQueue.student_id == student_id).where(StudentQueue.verdict == 'not_passed').order_by(StudentQueue.verdict_time).limit(1))
        return result.scalar_one_or_none()
    
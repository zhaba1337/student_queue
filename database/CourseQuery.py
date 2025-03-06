from typing import List, Any, Dict, Tuple
from typing_extensions import Self
from sqlalchemy import select, delete, update
from sqlalchemy.exc import PendingRollbackError, IntegrityError
from sqlalchemy.orm import load_only, selectinload

import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from models.Group import Group
from models.Course import Course
from .engine import Engine



class CourseQuery(Engine):
    async def GetById(self: Self, id: int) -> Course | None:
        result = await self.session().execute(select(Course).where(Course.id == id))
        return result.scalar_one_or_none()
    
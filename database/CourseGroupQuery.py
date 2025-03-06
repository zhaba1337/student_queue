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
from models.CourseGroup import CourseGroup
from .engine import Engine



class CourseGroupQuery(Engine):
    async def GetCourses(self: Self, group_id: int) -> List[Course]:
        courses_id = await self.session().execute(select(CourseGroup.course_id).where(CourseGroup.group_id == group_id))
        courses_id = courses_id.scalars().all()
        print(*courses_id)
        result = await self.session().execute(select(Course).options(selectinload(Course.teacher)).where(Course.id.in_(courses_id)))
        return result.scalars().all()
    
    async def GetGroups(self: Self, course_id: int) -> List[Group]:
        groups_id = await self.session().execute(select(CourseGroup).where(CourseGroup.course_id == course_id))
        groups_id = groups_id.scalars().all()
        result = await self.session().execute(select(Group).where(Group.id.in_(groups_id)))
        return result.scalars().all()
    

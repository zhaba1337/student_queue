from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from typing import List, Any
from typing_extensions import Self
from .Base import Base

class CourseGroup(Base):
    __tablename__ = 'course_group'
    
    course_id: Mapped[int] = mapped_column(Integer,  ForeignKey('courses.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from typing import List, Any
from typing_extensions import Self
from .Base import Base
from .Group import Group


association_table = Table('association_teacher_user', Base.metadata,
    Column('c_g_group_id', ForeignKey('course_group.id')),
    Column('group_id', ForeignKey('groups.id'))
)


class CourseGroup(Base):
    __tablename__ = 'course_group'
    
    course_id: Mapped[int] = mapped_column(Integer,  ForeignKey('courses.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    group_id: Mapped[int] = mapped_column(Integer, ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    
   # group: Mapped[Group] = relationship
from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from typing import List, Any
from typing_extensions import Self
from .Base import Base

class Lab(Base):
    __tablename__ = 'labs'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(Text, unique=True)
    description: Mapped[str] = mapped_column(Text, unique=True)
    course_id: Mapped[int] = mapped_column(Integer, ForeignKey('courses.id', ondelete='CASCADE', onupdate='CASCADE'))

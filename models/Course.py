from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from typing import List, Any
from typing_extensions import Self
from .Base import Base

class Course(Base):
    __tablename__ = 'courses'
    
    id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    teacher_id: Mapped[int] = mapped_column(Integer, ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False)
    cooldown_time: Mapped[int] = mapped_column(Integer, nullable=False)
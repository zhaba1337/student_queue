from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ENUM

from typing import List, Any
from typing_extensions import Self
from .Base import Base
from .VerdictEnum import VerdictEnum


class StudentQueue(Base):
    __tablename__ = 'student_queue'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    student_id: Mapped[int] = mapped_column(Integer, ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'), unique=False, nullable=False)
    lab_id: Mapped[int] = mapped_column(Integer, ForeignKey('labs.id', ondelete='CASCADE', onupdate='CASCADE'), unique=False, nullable=False)
    created_at: Mapped[int] = mapped_column(TIMESTAMP, nullable=False)
    verdict: Mapped[int] = mapped_column(ENUM(VerdictEnum, name='verdict_enum', create_type=False), nullable=True, )
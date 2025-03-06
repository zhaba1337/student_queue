
from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint, Table, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from typing import List, Any
from typing_extensions import Self
from .Base import Base
from .User import User



class Teacher(Base):
    __tablename__ = 'teachers'
    id: Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete='CASCADE', onupdate='CASCADE'), primary_key=True, nullable=False)
    user: Mapped[User] = relationship("User", lazy='selectin')
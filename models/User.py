
from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from typing import List, Any
from typing_extensions import Self
from .Base import Base

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False)
    family: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(255), nullable=True)
    
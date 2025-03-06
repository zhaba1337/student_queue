
from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from dataclasses import dataclass
from typing import List, Any
from typing_extensions import Self
from .Base import Base
import sys
import os

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from database.engine import Engine

class User(Base):
    
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=False)
    telegram_id: Mapped[int] = mapped_column(BigInteger, nullable=False, unique=True)
    family: Mapped[str] = mapped_column(String(255), nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    patronymic: Mapped[str] = mapped_column(String(255), nullable=True)
    
    def fullname(self: Self):
        return f"{self.family} {self.name} {self.patronymic}"
 
    

from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint, select, delete, update
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from typing import List, Any
from typing_extensions import Self
import sys
import os



class Base(DeclarativeBase):
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __str__(self):
        return str(self.as_dict())


from sqlalchemy import DateTime, Float, String, Text, func, Integer, BigInteger, TIMESTAMP, ForeignKey, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from typing import List, Any
from typing_extensions import Self


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    time_created: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    time_updated: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    
    # def __repr__(self: Self) -> List[Any]:
    #     return [self.time_created, self.time_updated]
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def __str__(self):
        return str(self.as_dict())
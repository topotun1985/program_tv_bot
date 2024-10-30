import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Text, Time, DateTime, func, INTEGER
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import time


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Programs(Base):
    __tablename__ = 'tvprograms'

    id: Mapped[int] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    channel_name: Mapped[str] = mapped_column(String(255), nullable=False)
    program_title: Mapped[str] = mapped_column(String(255), nullable=False)
    program_time: Mapped[time] = mapped_column(Time, nullable=False)

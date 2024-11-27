import uuid
from datetime import time, datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import String, Time, DateTime, func, INTEGER, ForeignKey, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Programs(Base):
    __tablename__ = 'tvprograms'

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    channel_name: Mapped[str] = mapped_column(String(255), nullable=False)
    program_title: Mapped[str] = mapped_column(String(255), nullable=False)
    program_time: Mapped[time] = mapped_column(Time, nullable=False)


class User(Base):
    __tablename__ = 'users'

    id = mapped_column(INTEGER, primary_key=True)
    user_id = mapped_column(String, unique=True, nullable=False)
    username = mapped_column(String)
    created = mapped_column(DateTime, default=func.now())
    updated = mapped_column(DateTime, default=func.now(), onupdate=func.now())

    favorites = relationship("UserFavorite", back_populates="user")
    donations = relationship("Donation", back_populates="user")



class UserFavorite(Base):
    __tablename__ = 'user_favorite'

    id = mapped_column(INTEGER, primary_key=True)
    user_id = mapped_column(String, ForeignKey('users.user_id'), nullable=False)
    channel_name = mapped_column(String, nullable=False)

    user = relationship("User", back_populates='favorites')


class Donation(Base):
    __tablename__ = 'donations'

    id = mapped_column(INTEGER, primary_key=True)
    user_id = mapped_column(String, ForeignKey('users.user_id'), nullable=False)
    amount = mapped_column(INTEGER, nullable=False)  # Количество звезд
    payment_id = mapped_column(String, unique=True)  # telegram_payment_charge_id
    timestamp = mapped_column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="donations")
    
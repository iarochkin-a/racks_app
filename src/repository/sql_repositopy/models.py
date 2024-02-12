from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from src.repository.sql_repositopy import Base


class RackORM(Base):
    __tablename__ = "racks"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    size: Mapped[int] = mapped_column(nullable=False)
    state: Mapped[str] = mapped_column(nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey("customers.id"))
    customer: Mapped["CustomerORM"] = relationship(back_populates="racks", lazy='selectin')
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    room: Mapped["RoomORM"] = relationship(back_populates="racks", lazy='selectin')


class RoomORM(Base):
    __tablename__ = 'rooms'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    racks: Mapped[list['RackORM']] = relationship(back_populates="room", lazy='selectin')


class CustomerORM(Base):
    __tablename__ = 'customers'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    racks: Mapped[list['RackORM']] = relationship(back_populates="customer", lazy='selectin')

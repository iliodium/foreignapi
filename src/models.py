from typing import Annotated

from sqlalchemy import String, ForeignKey, Integer, Sequence, Column, NUMERIC, Numeric, PrimaryKeyConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base, str_60, intpk, str_60_unique


class CustomerOrm(Base):
    __tablename__ = "customer"

    customer_id: Mapped[int] = mapped_column(Sequence('customer_customer_id_seq'), primary_key=True)
    name: Mapped[str_60_unique]

    menu: Mapped[list["MenuOrm"]] = relationship(
        back_populates="customer", lazy="selectin"
    )


class DishOrm(Base):
    __tablename__ = "dish"

    dish_id: Mapped[int] = mapped_column(Sequence('dish_dish_id_seq'), primary_key=True)
    name: Mapped[str_60_unique]

    menu: Mapped[list["MenuOrm"]] = relationship(
        back_populates="dish", lazy="selectin"
    )


class MenuOrm(Base):
    __tablename__ = "menu"
    __table_args__ = (
        PrimaryKeyConstraint('customer_id', 'dish_id'),
    )
    customer_id: Mapped[int] = mapped_column(ForeignKey("customer.customer_id"))
    dish_id: Mapped[int] = mapped_column(ForeignKey("dish.dish_id"))
    cost: Mapped[int]

    dish: Mapped["DishOrm"] = relationship(
        back_populates="menu", lazy="selectin"
    )
    customer: Mapped["CustomerOrm"] = relationship(
        back_populates="menu", lazy="selectin"
    )

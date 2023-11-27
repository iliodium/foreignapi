from typing import Annotated

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base, str_60, intpk



class CustomerOrm(Base):
    __tablename__ = "customer"
    __table_args__ = {'schema': 'public'}

    customer_id: Mapped[intpk]
    name: Mapped[str_60]
    auth: Mapped[str] = mapped_column(String(10))


class DishOrm(Base):
    __tablename__ = "dish"
    __table_args__ = {'schema': 'public'}

    dish_id: Mapped[intpk]
    name: Mapped[str_60]

    menu: Mapped["MenuOrm"] = relationship(
        back_populates="dish",
    )


class MenuOrm(Base):
    __tablename__ = "menu_key1"
    __table_args__ = {'schema': 'menu'}

    dish_id: Mapped[int] = mapped_column(ForeignKey("dish.dish_id"))
    cost: Mapped[float]

    dish: Mapped["DishOrm"] = relationship(
        back_populates="menu",
    )

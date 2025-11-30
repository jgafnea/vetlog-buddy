from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

"""Pet/Breed from CI SQL schema"""


class Breed(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    date_created: datetime
    name: str
    type: str
    pets: list["Pet"] = Relationship(back_populates="breed")


class Pet(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    birth_date: datetime
    date_created: datetime
    dewormed: Optional[bool] = None
    name: str
    status: str
    sterilized: Optional[bool] = None
    uuid: str
    vaccinated: Optional[bool] = None
    adopter_id: Optional[int] = None
    breed_id: Optional[int] = Field(default=None, foreign_key="breed.id")
    user_id: Optional[int] = None
    pet_id: Optional[int] = None

    breed: Optional[Breed] = Relationship(back_populates="pets")

    @property
    def weeks_old(self) -> int:
        """Pet's age in weeks"""
        return (datetime.now() - self.birth_date).days // 7

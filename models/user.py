# models/user.py
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import List


class Hobby(Enum):
    SPORTS = "Sports"
    READING = "Reading"
    MUSIC = "Music"


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birth_date: date
    subjects: List[str]
    hobby: Hobby
    picture_file: str
    address: str
    state: str
    city: str

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def birth_date_str(self) -> str:
        return self.birth_date.strftime("%d %B,%Y")

    @property
    def state_and_city(self) -> str:
        return f"{self.state} {self.city}"


# Предопределённый пользователь
student = User(
    first_name="Evgeniy",
    last_name="Student",
    email="Stud_Evg@example.com",
    phone_number="9321217654",
    birth_date=date(2000, 6, 15),
    subjects=["English"],
    hobby=Hobby.SPORTS,
    picture_file="test.jpg",
    address="Moscow, Russia",
    state="NCR",
    city="Delhi"
)
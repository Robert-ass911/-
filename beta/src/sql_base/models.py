from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Excursions(BaseModel):
    id: Optional[int]
    event: str
    Chart: str
    cost: int


class Exhibits(BaseModel):
    id: Optional[int]
    name: str
    Quantity: str
    Date_of_receipt:Optional[datetime]
    Condition: str
    author: str
    material: str


class Schedule(BaseModel):
    id: Optional[int]
    Work schedule: str
    time_of_the_event: int
    Pavilion: str


class Job_Title(BaseModel):
    id: Optional[int]
    name: str


class Services(BaseModel):
    id: Optional[int]
    name: str
    Price: int


class staff(BaseModel):
    id: Optional[int]
    Full_name: str
    Post: str
    Salary: str
    Education: str
    Phone number: str

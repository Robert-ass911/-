from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class Excursions(BaseModel):
    Excursion_id: Optional[int]
    Time_of_the_event:Optional[datetime]
    Chart: str
    cost: str


class Exhibits(BaseModel):
    Exhibit_id: Optional[int]
    name: str
    Quantity: str
    Date_of_receipt:Optional[datetime]
    Condition: str
    author: str
    material: str


class Schedule(BaseModel):
    Schedule_id: Optional[int]
    Work schedule: str
    time_of_the_event: int
    Pavilion: str


class Job_Title(BaseModel):
    Job_Title_id: Optional[int]
    name: str


class Services(BaseModel):
    Service_id: Optional[int]
    name: str
    Price: int


class staff(BaseModel):
    Personnel_id: Optional[int]
    Full_name: str
    Post: str
    Salary: str
    Education: str
    Phone number: str

from typing import Literal
from datetime import time
from pydantic import BaseModel

class TimeTableBase(BaseModel):
    day_id: int
    time_slot_id: int
    course_id: int

class TimeTableCreate(TimeTableBase):
    pass  # Used when creating a new timetable entry

class TimeTable(TimeTableBase):
    id: int

    class Config:
        orm_mode = True

from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time
from enrollement import * 


class TimeSlotBase(BaseModel):
    start_time: time
    end_time: time

class TimeSlotCreate(TimeSlotBase):
    pass  # Used when creating a new time slot

class TimeSlot(TimeSlotBase):
    id: int

    class Config:
        orm_mode = True
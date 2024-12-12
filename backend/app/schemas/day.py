from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time
from enrollement import * 

class DayBase(BaseModel):
    day_n: str

class DayCreate(DayBase):
    pass  # Used when creating a new day

class Day(DayBase):
    id: int

    class Config:
        orm_mode = True

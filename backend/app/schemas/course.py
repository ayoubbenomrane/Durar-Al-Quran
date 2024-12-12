from pydantic import BaseModel
from typing import List, Optional
from datetime import date, time
from .enrollement import * 
from .timeTable import *
# Base models

class CourseBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[float]
    teacher_id: Optional[int]

class CourseCreate(CourseBase):
    pass  # Used when creating a new course

class Course(CourseBase):
    id: int
    enrollments: List["Enrollment"] = []
    time_tables: List["TimeTable"] = []

    class Config:
        orm_mode = True


class CourseId(BaseModel):
    id:int
    class Config:
        orm_mode = True

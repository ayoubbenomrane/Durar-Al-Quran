from pydantic import BaseModel
from typing import List
from .course import *

class TeacherBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]

class TeacherCreate(TeacherBase):
    pass  # Used when creating a new teacher

class TeacherOut(TeacherBase):
    id: int
    courses: List["Course"] = []  # Include list of courses taught by the teacher

    class Config:
        orm_mode = True


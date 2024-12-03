from datetime import date
from pydantic import BaseModel
from .payment import *

class EnrollmentBase(BaseModel):
    student_id: int
    course_id: int
    enrollment_date: date

class EnrollmentCreate(EnrollmentBase):
    pass  # Used when creating a new enrollment

class Enrollment(EnrollmentBase):
    id: int
    payments: list["Payment"] = []

    class Config:
        orm_mode = True


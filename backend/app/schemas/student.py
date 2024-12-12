from pydantic import BaseModel,EmailStr
from typing import List,Optional
from .enrollement import *
class StudentBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email:  Optional[EmailStr]

class StudentCreate(StudentBase):
    email:EmailStr
    password:str
    class Config:
        orm_mode=True
    

class StudentLogin(BaseModel):
    email:EmailStr
    password:str

class Student(StudentBase):
    id: int
    enrollments: list["Enrollment"] = []  # Include list of enrollments

    class Config:
        orm_mode = True  # Enable ORM support for FastAPI

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date, Time
from sqlalchemy.orm import relationship
from .database import Base  

# Student table
class Student(Base):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    email=Column(String,nullable=False)
    password=Column(String,nullable=False)
    enrollments = relationship("Enrollment", back_populates="student")

# Teacher table
class Teacher(Base):
    __tablename__ = "teacher"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    courses = relationship("Course", back_populates="teacher")

# Course table
class Course(Base):
    __tablename__ = "course"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    teacher_id = Column(Integer, ForeignKey("teacher.id"))

    teacher = relationship("Teacher", back_populates="courses")
    enrollments = relationship("Enrollment", back_populates="course")
    time_tables = relationship("TimeTable", back_populates="course")

# Enrollment table
class Enrollment(Base):
    __tablename__ = "enrollment"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    course_id = Column(Integer, ForeignKey("course.id"))
    enrollment_date = Column(Date)

    student = relationship("Student", back_populates="enrollments")
    course = relationship("Course", back_populates="enrollments")
    payments = relationship("Payment", back_populates="enrollment")

# Payment table
class Payment(Base):
    __tablename__ = "payment"
    id = Column(Integer, primary_key=True, index=True)
    enrollment_id = Column(Integer, ForeignKey("enrollment.id"))
    payment_date = Column(Date)
    payment_month = Column(Date)

    enrollment = relationship("Enrollment", back_populates="payments")

# TimeTable table
class TimeTable(Base):
    __tablename__ = "time_table"
    id = Column(Integer, primary_key=True, index=True)
    day_id = Column(Integer, ForeignKey("days.id"))
    time_slot_id = Column(Integer, ForeignKey("time_slot.id"))
    course_id = Column(Integer, ForeignKey("course.id"))

    course = relationship("Course", back_populates="time_tables")
    days = relationship("Days", back_populates="time_tables")
    time_slot = relationship("TimeSlot", back_populates="time_tables")

# Day table
class Days(Base):
    __tablename__ = "days"
    id = Column(Integer, primary_key=True, index=True)
    day_name = Column(String)

    time_tables = relationship("TimeTable", back_populates="days")


# TimeSlot table
class TimeSlot(Base):
    __tablename__ = "time_slot"
    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(Time)
    end_time = Column(Time)

    time_tables = relationship("TimeTable", back_populates="time_slot")

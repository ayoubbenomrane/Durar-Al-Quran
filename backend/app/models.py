from sqlalchemy import Column, Integer, String, Text, DECIMAL, Date, ForeignKey, Time
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.types import Enum as SQLAlchemyEnum
from enum import Enum

Base = declarative_base()

# Define Enum Type for Day
class DayEnum(str, Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
    THURSDAY = "thursday"
    FRIDAY = "friday"
    SATURDAY = "saturday"
    SUNDAY = "sunday"

# Teacher Model
class Teacher(Base):
    __tablename__ = "teacher"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)

    # Relationships
    specializations = relationship("Specialization", back_populates="teacher")
    classes = relationship("Class", back_populates="teacher")
    assignments = relationship("Assignment", back_populates="teacher")

# Specialization Model
class Specialization(Base):
    __tablename__ = "specialization"

    id = Column(Integer, primary_key=True, index=True)
    specialization = Column(String(255), nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.id"), nullable=False)

    # Relationship
    teacher = relationship("Teacher", back_populates="specializations")

# Class Model
class Class(Base):
    __tablename__ = "class"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    price = Column(DECIMAL, nullable=False)
    teacher_id = Column(Integer, ForeignKey("teacher.id"))

    # Relationships
    teacher = relationship("Teacher", back_populates="classes")
    timetable = relationship("TimeTable", back_populates="class_ref")
    enrollments = relationship("Enrollment", back_populates="class_ref")
    assignments = relationship("Assignment", back_populates="class_ref")

# Time Table Model
class TimeTable(Base):
    __tablename__ = "time_table"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("class.id"), nullable=False)
    day = Column(SQLAlchemyEnum(DayEnum), nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    # Relationship
    class_ref = relationship("Class", back_populates="timetable")

# Student Model
class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    birthday = Column(Date)

    # Relationships
    enrollments = relationship("Enrollment", back_populates="student")
    payments = relationship("Payment", back_populates="student")

# Enrollment Model
class Enrollment(Base):
    __tablename__ = "enrollment"

    student_id = Column(Integer, ForeignKey("student.id"), primary_key=True)
    class_id = Column(Integer, ForeignKey("class.id"), primary_key=True)
    enrollment_date = Column(Date, nullable=False)

    # Relationships
    student = relationship("Student", back_populates="enrollments")
    class_ref = relationship("Class", back_populates="enrollments")

# Assignment Model
class Assignment(Base):
    __tablename__ = "assignment"

    teacher_id = Column(Integer, ForeignKey("teacher.id"), primary_key=True)
    class_id = Column(Integer, ForeignKey("class.id"), primary_key=True)
    assignment_date = Column(Date, nullable=False)

    # Relationships
    teacher = relationship("Teacher", back_populates="assignments")
    class_ref = relationship("Class", back_populates="assignments")

# Payment Model
class Payment(Base):
    __tablename__ = "payment"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"), nullable=False)
    class_id = Column(Integer, nullable=False)
    amount = Column(DECIMAL, nullable=False)
    payment_date = Column(Date, nullable=False)
    status = Column(String(50))

    # Relationships
    student = relationship("Student", back_populates="payments")
    # Foreign key for composite reference (assuming it's available in your database setup)
    __table_args__ = (
        ForeignKey("enrollment.student_id", "enrollment.class_id"),
    )

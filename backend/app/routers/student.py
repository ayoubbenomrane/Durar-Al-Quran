from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, utils, oauth2
from ..database import get_db
from ..schemas import student, course
from datetime import datetime

router = APIRouter()

# CREATE a student
@router.post("", response_model=student.Student)
def create_student(student: student.StudentCreate, db: Session = Depends(get_db)):
    hashed_password = utils.hash(student.password)
    student_data = student.model_dump()
    student_data["password"] = hashed_password
    new_student = models.Student(**student_data)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

# GET all students
@router.get("", response_model=list[student.Student])
def get_students(db: Session = Depends(get_db)):
    students = db.query(models.Student).all()
    return students

# GET a single student
@router.get("/{id}", response_model=student.Student)
def get_student(id: int, db: Session = Depends(get_db)):
    student_instance = db.query(models.Student).filter(models.Student.id == id).first()
    if not student_instance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id: {id} not found"
        )
    return student_instance

# UPDATE a student
@router.put("/{id}", response_model=student.StudentBase)
def update_student(id: int,updated_student: student.StudentBase,  db: Session = Depends(get_db)):

    student_query = db.query(models.Student).filter(models.Student.id == id)
    student_instance = student_query.first()
    if not student_instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Student with id: {id} not found")
    
    update_data = updated_student.model_dump(exclude_unset=True)

    student_query.update(update_data,synchronize_session=False)
    db.commit()
    return student_instance





    # DELETE a student
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_student(id: int, db: Session = Depends(get_db)):
    student_query = db.query(models.Student).filter(models.Student.id == id)
    student_instance = student_query.first()
    if not student_instance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Student with id: {id} not found"
        )
    student_query.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Student with id: {id} has been deleted"}



@router.post("/enroll", response_model=course.Enrollment)
def enroll_student( course_id: course.CourseId,current_student: int = Depends(oauth2.get_current_user),db: Session = Depends(get_db)):
    enrollment_date = datetime.now()
    new_enrollment = models.Enrollment(
        student_id=current_student.id,
        course_id=course_id.id,
        enrollment_date=enrollment_date
    )
    db.add(new_enrollment)
    db.commit()
    db.refresh(new_enrollment)
    return new_enrollment
from fastapi import FastAPI, HTTPException, status, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import engine, SessionLocal, get_db
from ..schemas import course
from .. import models

router = APIRouter(
        tags=['course']

)

# CREATE
@router.post("/", response_model=course.CourseCreate)
def create_course(course: course.CourseCreate, db: Session = Depends(get_db)):
    new_course = models.Course(**course.model_dump())
    db.add(new_course)
    db.commit()
    db.refresh(new_course)  # Refresh to get the generated ID and other fields
    return new_course


# add time table


# READ ALL
@router.get("/", response_model=list[course.Course])
def get_courses(db: Session = Depends(get_db)):
    courses = db.query(models.Course).all()
    return courses

# READ SINGLE
@router.get("/{id}", response_model=course.Course)
def get_course(id: int, db: Session = Depends(get_db)):
    course = db.query(models.Course).filter(models.Course.id == id).first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id: {id} not found"
        )
    return course

# UPDATE
@router.put("/{id}", response_model=course.CourseCreate)
def update_course( id: int,updated_course: course.CourseBase, db: Session = Depends(get_db)):
    course_query = db.query(models.Course).filter(models.Course.id == id)
    course = course_query.first()
    if not course:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Course with id: {id} not found")
    course_query.update(updated_course.model_dump(), synchronize_session=False)
    db.commit()
    db.refresh(course)
    return course

# DELETE
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_course(id: int, db: Session = Depends(get_db)):
    course_query = db.query(models.Course).filter(models.Course.id == id)
    course = course_query.first()
    if not course:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Course with id: {id} not found"
        )
    course_query.delete(synchronize_session=False)
    db.commit()
    return {"message": f"Course with id: {id} has been deleted"}

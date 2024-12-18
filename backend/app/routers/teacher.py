from .. import models
from fastapi import FastAPI , Depends, APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import teacher

router=APIRouter(
        tags=['teacher']

)


@router.post("", response_model=teacher.TeacherOut)
def add_teacher(teacher: teacher.TeacherCreate, db: Session = Depends(get_db)):
    db_teacher = models.Teacher(**teacher.model_dump())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    # Return the teacher with the generated ID
    return db_teacher

# see existing teachers 
@router.get("",response_model=list[teacher.TeacherOut])
def get_teachers(db:Session=Depends(get_db)):
    res=db.query(models.Teacher).all()
    return res


# see teacher by id 
@router.get("/{id}", response_model=teacher.TeacherOut)
def get_teacher(id: int, db: Session = Depends(get_db)):
    teacher_instance = db.query(models.Teacher).filter(models.Teacher.id == id).first()
    if not teacher_instance:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Teacher with id: {id} not found")
    return teacher_instance


@router.put("/{id}",response_model=teacher.TeacherOut)
def update_teacher(id:int, updated_teacher:teacher.TeacherBase,db:Session=Depends(get_db)):
    teacher_query=db.query(models.Teacher).filter(models.Teacher.id==id)
    teacher=teacher_query.first()
    if not teacher:
        raise HTTPException(  status_code=status.HTTP_404_NOT_FOUND, detail=f"Teacher with id: {id} not found")
    teacher_query.update(updated_teacher.model_dump(),synchronize_session=False)
    db.commit()
    db.refresh(teacher)
    return teacher



# Delete a teacher (DELETE)
@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_teacher(id: int, db: Session = Depends(get_db)):
    teacher_instance = db.query(models.Teacher).filter(models.Teacher.id == id).first()
    if not teacher_instance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Teacher with id: {id} not found"
        )
    db.delete(teacher_instance)
    db.commit()
    return {"message": f"Teacher with id: {id} has been deleted"}



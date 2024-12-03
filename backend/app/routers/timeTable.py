from .. import models
from fastapi import FastAPI , Depends, APIRouter,HTTPException,status
from sqlalchemy.orm import Session
from ..database import get_db
from ..schemas import timeTable

router=APIRouter()


@router.post("/", response_model=timeTable.TimeTable)
def create_time_table(time_table_data: timeTable.TimeTableCreate, db: Session = Depends(get_db)):

    new_time_table = models.TimeTable(**time_table_data.model_dump())
    db.add(new_time_table)
    db.commit()
    db.refresh(new_time_table)  # Ensure the ID is fetched after commit
    
    return new_time_table



@router.delete("/{id}")
def delete_time_table(id:int, db:Session=Depends(get_db)):
    time_table_query=db.query(models.TimeTable).filter(models.TimeTable.id==id).first()
    if not time_table_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"time table with id {id} not found")
    db.delete(time_table_query)
    db.commit()
    
    return {"message":"time table deleted"}
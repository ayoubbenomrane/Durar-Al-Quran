from fastapi import APIRouter,Depends,status,HTTPException,Response
from ..database import engine,SessionLocal,get_db
from sqlalchemy.orm import Session
from .. import utils,oauth2,models
from ..schemas import authentication

from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(
    tags=['authentification']
)

@router.post('/login',response_model=authentication.Token)
def login(user_credentials:OAuth2PasswordRequestForm=Depends(),db:Session=Depends(get_db)):
    user= db.query(models.Student).filter(
        models.Student.email==user_credentials.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not valid email")
    
    if not utils.verify(user_credentials.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"invalid credentials")
    access_token=oauth2.create_access_token(data={"user_id":user.id})
    return {"access_token": access_token,"token_type":"bearer"}







# main.py
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import auth,student,course,teacher,timeTable

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(auth.router)
app.include_router(student.router,prefix="/student")
app.include_router(course.router,prefix="/course")
app.include_router(teacher.router,prefix="/teacher")
app.include_router(timeTable.router,prefix="/timeTable")

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to the Quran Learning Platform!"}

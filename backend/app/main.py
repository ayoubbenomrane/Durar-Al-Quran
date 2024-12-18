# main.py
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import auth,student,course,teacher,timeTable
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, replace "" with specific domains in production
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods: GET, POST, PUT, etc.
    allow_headers=["*"],  # Allows all headers
)

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

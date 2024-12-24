from fastapi import FastAPI
from .routes import users


app = FastAPI()

# app.include_router(users.router)

student = {
    1: {
        "Name": "Anubhav",
        "age":"23",
        "class":"Developer"
    }
}

@app.get("/get_students/{student}")
def get_student(student_id: int):
    return student[student_id]
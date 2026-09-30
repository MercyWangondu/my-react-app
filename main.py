from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Hello, this is my API!"}

@app.get("/student")
def get_student():
    return {
        "name": "Mercy",
        "course": "BSc Informatics and Computer Science",
        "university": "Strathmore University"
    }

@app.post("/student")
def create_student(student: dict):
    return {
        "message": "Student created successfully",
        "student": student
    }
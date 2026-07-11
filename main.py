from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}
    
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}

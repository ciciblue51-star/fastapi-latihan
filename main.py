from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}
    
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id": student_id}

@app.get("/search")
def search(keyword: str, limit: int = 10):
    return {"keyword": keyword, "limit": limit}


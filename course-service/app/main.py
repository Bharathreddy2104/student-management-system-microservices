from fastapi import FastAPI

app = FastAPI(title="Course Service")

@app.get("/")
def home():
    return {"message": "Course Service"}

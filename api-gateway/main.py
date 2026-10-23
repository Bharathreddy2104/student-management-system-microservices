from fastapi import FastAPI

app = FastAPI(title="API Gateway")

@app.get("/")
def home():
    return {"message": "Student Management System API Gateway"}

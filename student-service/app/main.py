from fastapi import FastAPI

app = FastAPI(title="Student Service")

@app.get("/")
def home():
    return {"message": "Student Service"}

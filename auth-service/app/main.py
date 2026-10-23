from fastapi import FastAPI

app = FastAPI(title="Authentication Service")

@app.get("/")
def home():
    return {"message": "Authentication Service"}

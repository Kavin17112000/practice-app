from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Backend Running Successfully"
    }

@app.get("/api/health")
def health():
    return {
        "status": "UP"
    }
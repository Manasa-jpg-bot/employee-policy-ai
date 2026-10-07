from fastapi import FastAPI

app = FastAPI(
    title="Employee Policy AI Assistant",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Employee Policy AI Assistant"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
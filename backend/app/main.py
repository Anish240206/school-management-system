from fastapi import FastAPI

app = FastAPI(
    title="School Management System API",
    description="Backend API for the School Management System.",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    return {"status": "healthy"}
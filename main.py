from fastapi import FastAPI

app = FastAPI(
    title="WeatherWise API",
    description="City-based Weather Advisory API",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {
        "message": "WeatherWise API Running"
    }

@app.get("/health")
async def health_check():
    return {
        "status": "ok"
    }
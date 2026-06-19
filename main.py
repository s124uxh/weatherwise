from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.weather import router as weather_router

app = FastAPI(
    title="WeatherWise API",
    version="1.0.0",
    description="City-based Weather Advisory API"
)
app.include_router(weather_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "WeatherWise API Running"}

@app.get("/health")
async def health():
    return {"status": "ok"}
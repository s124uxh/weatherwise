import httpx
from core.logging import logger

WEATHER_URL = "https://api.open-meteo.com/v1/forecast"


async def get_current_weather(
    latitude: float,
    longitude: float
):

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code,wind_speed_10m"
    }
    logger.info(
    f"Fetching weather for latitude={latitude}, longitude={longitude}"
)

    async with httpx.AsyncClient(timeout=10.0) as client:

        response = await client.get(
            WEATHER_URL,
            params=params
        )

        response.raise_for_status()
        logger.info(
    "Weather API request successful"
)

    data = response.json()

    current = data["current"]
    logger.info(
    "Weather data processed successfully"
)

    return {
        "temperature": current["temperature_2m"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": current["weather_code"]
    }
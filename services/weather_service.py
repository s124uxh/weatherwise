import httpx

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

    async with httpx.AsyncClient(timeout=10.0) as client:

        response = await client.get(
            WEATHER_URL,
            params=params
        )

        response.raise_for_status()

    data = response.json()

    current = data["current"]

    return {
        "temperature": current["temperature_2m"],
        "wind_speed": current["wind_speed_10m"],
        "weather_code": current["weather_code"]
    }
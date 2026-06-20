import httpx

from core.logging import logger

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"


async def get_city_coordinates(city: str):

    logger.info(
        f"Searching coordinates for city: {city}"
    )

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    async with httpx.AsyncClient(timeout=10.0) as client:

        response = await client.get(
            GEOCODING_URL,
            params=params
        )

        response.raise_for_status()

        logger.info(
            "Geocoding API request successful"
        )

    data = response.json()

    results = data.get("results")

    if not results:

        logger.warning(
            f"City not found: {city}"
        )

        return None

    city_data = results[0]

    logger.info(
        f"Coordinates found for city: {city}"
    )

    return {
        "name": city_data["name"],
        "country": city_data["country"],
        "latitude": city_data["latitude"],
        "longitude": city_data["longitude"],
        "timezone": city_data["timezone"]
    }
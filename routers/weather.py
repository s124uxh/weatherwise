from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from core.logging import logger

from services.geocoding_service import get_city_coordinates
from services.weather_service import get_current_weather
from services.advisory_service import generate_advisory

router = APIRouter(
    prefix="/weather",
    tags=["Weather"]
)


@router.get("/current")
async def current_weather(city: str):

    logger.info(
        f"/weather/current requested for city={city}"
    )

    location = await get_city_coordinates(city)

    if not location:

        logger.warning(
            f"City not found: {city}"
        )

        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    weather = await get_current_weather(
        location["latitude"],
        location["longitude"]
    )

    advisory = generate_advisory(
        weather["temperature"],
        weather["wind_speed"],
        weather["weather_code"]
    )

    logger.info(
        f"Current weather response generated for city={city}"
    )

    return {
        "city": city,
        "temperature_celsius": weather["temperature"],
        "wind_speed": weather["wind_speed"],
        "condition": advisory["condition"],
        "source": "open-meteo"
    }


@router.get("/advisory")
async def weather_advisory(city: str):

    logger.info(
        f"/weather/advisory requested for city={city}"
    )

    location = await get_city_coordinates(city)

    if not location:

        logger.warning(
            f"City not found: {city}"
        )

        raise HTTPException(
            status_code=404,
            detail="City not found"
        )

    weather = await get_current_weather(
        location["latitude"],
        location["longitude"]
    )

    advisory = generate_advisory(
        weather["temperature"],
        weather["wind_speed"],
        weather["weather_code"]
    )

    logger.info(
        f"Weather advisory response generated for city={city}"
    )

    return {
        "city": city,
        "location": location,
        "weather": {
            "temperature_celsius": weather["temperature"],
            "wind_speed": weather["wind_speed"],
            "condition": advisory["condition"],
            "is_raining": advisory["is_raining"]
        },
        "advisory": {
            "message": advisory["message"],
            "level": advisory["level"]
        },
        "source": "open-meteo",
        "timestamp": datetime.now(timezone.utc)
    }
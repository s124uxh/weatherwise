from utils.weather_codes import WEATHER_CODES
from core.logging import logger


def generate_advisory(
    temperature: float,
    wind_speed: float,
    weather_code: int
):

    logger.info(
        f"Generating advisory for weather_code={weather_code}"
    )

    condition = WEATHER_CODES.get(
        weather_code,
        "Unknown"
    )

    is_raining = weather_code in [
        51, 53, 55,
        61, 63, 65,
        80, 81, 82
    ]

    if weather_code in [95, 96, 99]:

        logger.warning(
            "Thunderstorm advisory generated"
        )

        return {
            "message": "Thunderstorm expected. Avoid outdoor activities if possible.",
            "level": "alert",
            "condition": condition,
            "is_raining": True
        }

    if temperature > 40:

        logger.warning(
            "Extreme heat advisory generated"
        )

        return {
            "message": "Extreme heat. Avoid going out if possible.",
            "level": "alert",
            "condition": condition,
            "is_raining": is_raining
        }

    if temperature > 35:

        logger.warning(
            "High temperature advisory generated"
        )

        return {
            "message": "It is very hot. Stay hydrated.",
            "level": "caution",
            "condition": condition,
            "is_raining": is_raining
        }

    if is_raining:

        logger.info(
            "Rain advisory generated"
        )

        return {
            "message": "Carry an umbrella.",
            "level": "caution",
            "condition": condition,
            "is_raining": is_raining
        }

    if wind_speed > 30:

        logger.info(
            "Wind advisory generated"
        )

        return {
            "message": "It may be windy outside.",
            "level": "caution",
            "condition": condition,
            "is_raining": is_raining
        }

    logger.info(
        "Normal weather advisory generated"
    )

    return {
        "message": "Good weather for going out.",
        "level": "normal",
        "condition": condition,
        "is_raining": is_raining
    }
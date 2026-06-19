from utils.weather_codes import WEATHER_CODES


def generate_advisory(
    temperature: float,
    wind_speed: float,
    weather_code: int
):

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
        return {
            "message": "Thunderstorm expected. Avoid outdoor activities if possible.",
            "level": "alert",
            "condition": condition,
            "is_raining": True
        }

    if temperature > 40:
        return {
            "message": "Extreme heat. Avoid going out if possible.",
            "level": "alert",
            "condition": condition,
            "is_raining": is_raining
        }

    if temperature > 35:
        return {
            "message": "It is very hot. Stay hydrated.",
            "level": "caution",
            "condition": condition,
            "is_raining": is_raining
        }

    if is_raining:
        return {
            "message": "Carry an umbrella.",
            "level": "caution",
            "condition": condition,
            "is_raining": is_raining
        }

    if wind_speed > 30:
        return {
            "message": "It may be windy outside.",
            "level": "caution",
            "condition": condition,
            "is_raining": is_raining
        }

    return {
        "message": "Good weather for going out.",
        "level": "normal",
        "condition": condition,
        "is_raining": is_raining
    }
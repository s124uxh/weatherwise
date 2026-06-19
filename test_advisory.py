from services.advisory_service import generate_advisory


result = generate_advisory(
    temperature=32.4,
    wind_speed=10.4,
    weather_code=95
)

print(result)
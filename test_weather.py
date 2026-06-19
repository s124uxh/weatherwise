import asyncio

from services.weather_service import get_current_weather


async def main():

    result = await get_current_weather(
        latitude=22.56263,
        longitude=88.36304
    )

    print(result)


asyncio.run(main())
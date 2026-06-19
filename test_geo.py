import asyncio

from services.geocoding_service import get_city_coordinates


async def main():
    result = await get_city_coordinates("Kolkata")
    print(result)


asyncio.run(main())
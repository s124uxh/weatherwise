import asyncio
import httpx


async def main():

    async with httpx.AsyncClient() as client:

        response = await client.get(
            "https://geocoding-api.open-meteo.com/v1/search",
            params={
                "name": "Kolkata",
                "count": 1
            }
        )

        print(response.status_code)
        print(response.json())


asyncio.run(main())
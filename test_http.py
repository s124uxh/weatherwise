import requests

response = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search?name=Kolkata&count=1"
)

print(response.status_code)
print(response.json())
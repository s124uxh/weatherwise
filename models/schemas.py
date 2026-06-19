from pydantic import BaseModel


class LocationSchema(BaseModel):
    name: str
    country: str
    latitude: float
    longitude: float
    timezone: str


class WeatherSchema(BaseModel):
    temperature_celsius: float
    wind_speed: float
    condition: str
    is_raining: bool


class AdvisorySchema(BaseModel):
    message: str
    level: str


class WeatherAdvisoryResponse(BaseModel):
    city: str
    location: LocationSchema
    weather: WeatherSchema
    advisory: AdvisorySchema
    source: str
    timestamp: str


class CurrentWeatherResponse(BaseModel):
    city: str
    temperature_celsius: float
    wind_speed: float
    condition: str
    source: str
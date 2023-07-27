from pydantic import BaseModel


class WeatherDataEntity(BaseModel):
    observation_time: str
    timezone: str
    precipitation: float
    wind_speed: float
    wind_direction: str
    temperature: float
    cloud_coverage: int
    description: str

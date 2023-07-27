from pydantic import BaseModel, Extra


class WeatherData(BaseModel):
    ob_time: str
    timezone: str
    precip: float
    wind_spd: float
    wind_cdir_full: str
    temp: float
    clouds: int
    weather: dict

    class Config:
        extra = Extra.allow

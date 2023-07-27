from pydantic_factories import ModelFactory

from tracking_api.adapters.weather_bit_api_repository.schemas import WeatherData


class WeatherDataFactory(ModelFactory):
    __model__ = WeatherData

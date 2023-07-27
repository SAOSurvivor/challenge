from pydantic_factories import ModelFactory

from tracking_api.domain.entities import WeatherDataEntity


class WeatherDataEntityFactory(ModelFactory):
    __model__ = WeatherDataEntity

from pydantic_factories import ModelFactory

from tracking_api.domain.entities import ShipmentsWithWeatherDataEntity


class ShipmentsWithWeatherDataEntityFactory(ModelFactory):
    __model__ = ShipmentsWithWeatherDataEntity

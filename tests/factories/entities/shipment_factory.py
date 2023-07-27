from pydantic_factories import ModelFactory

from tracking_api.domain.entities import ShipmentEntity


class ShipmentEntityFactory(ModelFactory):
    __model__ = ShipmentEntity

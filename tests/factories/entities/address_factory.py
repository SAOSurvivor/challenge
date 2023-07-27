from pydantic_factories import ModelFactory

from tracking_api.domain.entities import AddressEntity


class AddressEntityFactory(ModelFactory):
    __model__ = AddressEntity

from tracking_api.adapters.sql_repository.models import (
    Address as AddressModel,
    Shipment as ShipmentModel,
)
from tracking_api.domain.entities import AddressEntity, ShipmentEntity


class ShipmentMapper:
    """A Mapper class to map shipment schemas between the domain and the repository."""

    @staticmethod
    def from_entity_to_model(
        shipment: ShipmentEntity, sender_address_id: int, receiver_address_id: int
    ) -> ShipmentModel:
        """
        A mapper that maps a shipment entity to shipment model.

        @param shipment: input shipment entity
        @param sender_address_id: id corresponding to sender address
        @param receiver_address_id: id corresponding to receiver address

        @return : a shipment model object created from shipment entity
        """
        shipment_model = ShipmentModel(
            tracking_number=shipment.tracking_number,
            carrier=shipment.carrier,
            sender_address_id=sender_address_id,
            receiver_address_id=receiver_address_id,
            article_name=shipment.article_name,
            article_quantity=shipment.article_quantity,
            article_price=shipment.article_price,
            sku=shipment.sku,
            status=shipment.status,
        )
        return shipment_model

    @staticmethod
    def from_model_to_entity(
        shipment_model: ShipmentModel,
        sender_address: AddressModel,
        receiver_address: AddressModel,
    ) -> ShipmentEntity:
        """
        A mapper that maps a shipment, and address models to shipment entity
        @param shipment_model: input shipment model
        @param sender_address: address model object containing the sender's location
        @param receiver_address: address model object containing the receiver's location

        @return : a shipment entity object created from shipment model
        """
        shipment_entity = ShipmentEntity(
            tracking_number=shipment_model.tracking_number,
            carrier=shipment_model.carrier,
            sender_address=AddressMapper.from_model_to_entity(sender_address),
            receiver_address=AddressMapper.from_model_to_entity(receiver_address),
            article_name=shipment_model.article_name,
            article_quantity=shipment_model.article_quantity,
            article_price=shipment_model.article_price,
            sku=shipment_model.sku,
            status=shipment_model.status,
        )
        return shipment_entity


class AddressMapper:
    """
    A Mapper class to map address schemas between the domain and the repository
    """

    @staticmethod
    def from_entity_to_model(address: AddressEntity) -> AddressModel:
        """
        A mapper that maps a address entity to address model
        @param address: input address entity

        @return : an address model object created from address entity
        """
        address_model = AddressModel(
            street=address.street,
            house_no=address.house_no,
            city=address.city,
            pin_code=address.pin_code,
            country=address.country,
        )
        return address_model

    @staticmethod
    def from_model_to_entity(address_model: AddressModel) -> AddressEntity:
        """
        A mapper that maps an address model to entity
        @param address_model: input address model

        @return : an address entity created from shipment model
        """
        address_entity = AddressEntity(
            id=address_model.id,
            street=address_model.street,
            house_no=address_model.house_no,
            city=address_model.city,
            pin_code=address_model.pin_code,
            country=address_model.country,
        )
        return address_entity

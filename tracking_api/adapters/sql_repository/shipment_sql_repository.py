from typing import List

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import scoped_session

from tracking_api.adapters.sql_repository import mappers, models
from tracking_api.adapters.sql_repository.mappers import AddressMapper, ShipmentMapper
from tracking_api.adapters.sql_repository.models import Address, Shipment
from tracking_api.domain import ports
from tracking_api.domain.entities import AddressEntity, ShipmentEntity
from tracking_api.domain.entities.exceptions import AddressNotFound, ShipmentNotFound


class ShipmentSQLRepository(ports.ShipmentRepository):
    """
    The implementation of Shipment Repository use to access SQL Data
    """

    def __init__(self, db_session: scoped_session):
        self.db_session = db_session

    def init(self) -> None:
        models.Base.metadata.create_all(self.db_session.get_bind())

    def create(
        self,
        shipment_entity: ShipmentEntity,
        sender_address: AddressEntity,
        receiver_address: AddressEntity,
    ):
        try:
            sender_address = AddressMapper.from_entity_to_model(sender_address)
            receiver_address = AddressMapper.from_entity_to_model(receiver_address)
            self.db_session.add(sender_address)
            self.db_session.add(receiver_address)
            self.db_session.flush()

            shipment = ShipmentMapper.from_entity_to_model(
                shipment_entity, sender_address.id, receiver_address.id
            )
            self.db_session.add(shipment)

            self.db_session.commit()
        except Exception:
            self.db_session.rollback()

    def get_shipments(self, carrier: str, tracking_number: str) -> List[ShipmentEntity]:
        """
        Fetches a list of shipments based on the carrier and tracking number, maps it to ShipmentEntity and then returns it

        @param carrier: the shipment carrier
        @param tracking_number: unique id to track a package

        returns: a list of shipment entities that fulfill the above conditions
        """

        try:
            shipment_entities = []
            shipment_models = (
                self.db_session.query(Shipment)
                .filter(
                    Shipment.carrier == carrier,
                    Shipment.tracking_number == tracking_number,
                )
                .all()
            )
            if not shipment_models:
                raise ShipmentNotFound(carrier, tracking_number)

            for shipment_model in shipment_models:
                sender_address = (
                    self.db_session.query(Address)
                    .filter(Address.id == shipment_model.sender_address_id)
                    .first()
                )
                receiver_address = (
                    self.db_session.query(Address)
                    .filter(Address.id == shipment_model.receiver_address_id)
                    .first()
                )

                if not sender_address or not receiver_address:
                    raise AddressNotFound()

                shipment_entity = mappers.ShipmentMapper.from_model_to_entity(
                    shipment_model, sender_address, receiver_address
                )
                shipment_entities.append(shipment_entity)
        except SQLAlchemyError as exception:
            raise exception

        return shipment_entities

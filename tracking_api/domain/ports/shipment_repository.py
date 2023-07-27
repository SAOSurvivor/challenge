import abc
from typing import List

from tracking_api.domain.entities import AddressEntity
from tracking_api.domain.entities.shipment import ShipmentEntity


class ShipmentRepository(abc.ABC):
    @abc.abstractmethod
    def init(self) -> None:
        pass

    @abc.abstractmethod
    def create(
        self,
        shipment_entity: ShipmentEntity,
        sender_address: AddressEntity,
        receiver_address: AddressEntity,
    ) -> None:
        pass

    @abc.abstractmethod
    def get_shipments(self, carrier: str, tracking_number: str) -> List[ShipmentEntity]:
        pass

from pydantic import BaseModel

from tracking_api.domain.entities.address import AddressEntity


class ShipmentEntity(BaseModel):
    tracking_number: str
    carrier: str
    sender_address: AddressEntity
    receiver_address: AddressEntity
    article_name: str
    article_quantity: int
    article_price: float
    sku: str
    status: str

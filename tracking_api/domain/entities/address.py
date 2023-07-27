from pydantic import BaseModel


class AddressEntity(BaseModel):
    street: str
    house_no: str
    city: str
    pin_code: str
    country: str

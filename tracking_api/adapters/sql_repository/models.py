from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class Address(Base):
    __tablename__ = "address"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    street: str = Column(String, nullable=False)
    house_no: str = Column(String, nullable=False)
    city: str = Column(String, nullable=False)
    pin_code: str = Column(String, nullable=False)
    country: str = Column(String, nullable=False)


class Shipment(Base):
    __tablename__ = "shipment"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    tracking_number: str = Column(String, nullable=False)
    carrier: str = Column(String, nullable=False)
    sender_address_id: int = Column(Integer, nullable=False)
    receiver_address_id: int = Column(Integer, nullable=False)
    article_name: str = Column(String, nullable=False)
    article_quantity: int = Column(Integer, nullable=False)
    article_price: int = Column(Float, nullable=False)
    sku: int = Column(String, nullable=False)
    status: str = Column(String, nullable=False)

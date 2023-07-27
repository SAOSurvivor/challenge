import json
import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool

from tests.factories.entities.address_factory import AddressEntityFactory
from tests.factories.entities.shipment_factory import ShipmentEntityFactory
from tests.factories.schemas.weather_api_schema_factory import WeatherDataFactory
from tracking_api import adapters
from tracking_api.adapters.weather_bit_api_repository.mappers import WeatherDataMapper
from tracking_api.domain import ports, use_cases
from tracking_api.domain.entities import WeatherDataEntity


def get_address_attributes_from_address_string(address_string: str) -> dict:
    """
    Extracts address fields from the given address string.

    @param address_string: address string
    """
    address_parts = address_string.split(",")
    address_dict = {
        "street": address_parts[0].strip().split(" ")[0],
        "house_no": address_parts[0].strip().split(" ")[1],
        "pin_code": address_parts[1].strip().split(" ")[0],
        "city": address_parts[1].strip().split(" ")[1],
        "country": address_parts[2].strip(),
    }
    return address_dict


def seed_db(db_session: scoped_session):
    """
    Seeds the test db with data from data/db_seed_data.json.

    @param db_session: test db session
    """
    shipment_repository = adapters.ShipmentSQLRepository(db_session)
    shipment_repository.init()
    seed_data_json = json.load(
        open(
            os.path.abspath(
                os.path.join(os.path.dirname(__file__), "data", "db_seed_data.json")
            )
        )
    )
    for shipment_dict in seed_data_json:
        sender_address = AddressEntityFactory.build(
            **get_address_attributes_from_address_string(
                shipment_dict["sender_address"]
            )
        )
        receiver_address = AddressEntityFactory.build(
            **get_address_attributes_from_address_string(
                shipment_dict["receiver_address"]
            )
        )
        del shipment_dict["sender_address"]
        del shipment_dict["receiver_address"]
        shipment = ShipmentEntityFactory.build(**shipment_dict)
        shipment_repository.create(shipment, sender_address, receiver_address)


@pytest.fixture
def db_session() -> scoped_session:
    """Creates a db session to be used by the tests."""
    in_memory_engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    _session_factory = sessionmaker(
        autocommit=False, autoflush=True, bind=in_memory_engine
    )
    db_session: scoped_session = scoped_session(_session_factory)
    seed_db(db_session)
    return db_session


class WeatherTestRepository(object):
    """A test repository that mocks the weather api repository. It returns weather data from sample json."""

    def __init__(self):
        self.data = json.load(
            open(
                os.path.join(
                    os.path.dirname(__file__),
                    "data",
                    "weather_repository_seed_data.json",
                )
            )
        )

    def get_weather_data_by_zip_country(
        self, zip_code: str, country: str
    ) -> WeatherDataEntity:
        for weather_data_dict in self.data:
            if (
                weather_data_dict["input_pin_code"] == zip_code
                and weather_data_dict["input_country"] == country
            ):
                weather_data = WeatherDataFactory.build(**weather_data_dict)
                weather_data_entity = WeatherDataMapper.from_api_schema_to_entity(
                    weather_data
                )
                return weather_data_entity


@pytest.fixture
def shipment_repository(db_session: scoped_session) -> ports.ShipmentRepository:
    """
    Fixture that creates a shipment_repository with test db adapter.

    @param db_session: Test DB session
    """
    shipment_repository = adapters.ShipmentSQLRepository(db_session)
    shipment_repository.init()
    return shipment_repository


@pytest.fixture
def weather_repository() -> WeatherTestRepository:
    """
    Fixture that creates a weather_repository with a mocked weather api.

    @return: Test Weather repository
    """
    weather_repository = WeatherTestRepository()
    return weather_repository


@pytest.fixture
def retrieve_shipments_with_weather_data_use_case(
    shipment_repository: ports.ShipmentRepository,
    weather_repository: ports.WeatherRepository,
) -> use_cases.RetrieveShipmentsWithWeatherData:
    """Fixture that returns a use case object for retrieving shipments, initialized with mocked repositories."""
    return use_cases.RetrieveShipmentsWithWeatherData(
        shipment_repository, weather_repository
    )

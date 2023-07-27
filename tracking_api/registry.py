import logging
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from tracking_api import adapters, settings
from tracking_api.domain import use_cases


# SqlAlchemy logging
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
_handler = logging.StreamHandler(sys.stdout)
_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(_handler)

# Database connection
postgres_engine = create_engine(
    settings.DATABASE_CONNECTION_STRING,
    echo=True,
)
_session_factory = sessionmaker(autocommit=False, autoflush=True, bind=postgres_engine)
_db_session: scoped_session = scoped_session(_session_factory)


# Adapters
_sql_alchemy_shipment_repository = adapters.ShipmentSQLRepository(_db_session)
_weather_api_repository = adapters.WeatherApiRepository(
    settings.WEATHER_BIT_URL[0], settings.WEATHER_BIT_API_KEY
)

# Use cases
retrieve_shipment_use_case = use_cases.RetrieveShipmentsWithWeatherData(
    _sql_alchemy_shipment_repository, _weather_api_repository
)

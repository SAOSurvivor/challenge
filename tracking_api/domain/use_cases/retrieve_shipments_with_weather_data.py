from tracking_api.domain import ports
from tracking_api.domain.entities.shipments_with_weather_data import ShipmentsWithWeatherDataEntity


class RetrieveShipmentsWithWeatherData:
    """
    Class representing the use case for extracting shipment information with weather data
    """

    def __init__(
        self,
        shipment_repository: ports.ShipmentRepository,
        weather_repository: ports.WeatherRepository,
    ):
        """
        This class is initialized with a shipment and weather repository as we require data from two sources
        """
        self.shipment_repository = shipment_repository
        self.weather_repository = weather_repository

    def perform(self, carrier: str, tracking_number: str) -> dict:
        """
        Business logic to fetch data from shipment repo, and weather repo and then combine them
        """
        shipment_with_weather_data_dict = {}
        shipments = self._get_shipments(carrier, tracking_number)
        weather_data = self._get_weather_data(
            shipments[0].receiver_address.pin_code, shipments[0].receiver_address.country
        )

        shipment_with_weather_data_dict["shipments"] = [shipment.dict() for shipment in shipments]
        shipment_with_weather_data_dict["destination_weather"] = weather_data.dict()

        shipment_with_weather_data = ShipmentsWithWeatherDataEntity(
            **shipment_with_weather_data_dict
        )
        return shipment_with_weather_data.dict()

    def _get_shipments(self, carrier, tracking_number):
        shipments = self.shipment_repository.get_shipments(carrier, tracking_number)
        return shipments

    def _get_weather_data(self, pin_code, country):
        weather_data = self.weather_repository.get_weather_data_by_zip_country(
            pin_code, country
        )
        return weather_data

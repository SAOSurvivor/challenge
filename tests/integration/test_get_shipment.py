from unittest.mock import patch

from tracking_api.controllers.flask_api import app
from tracking_api.domain import use_cases


class TestGetShipmentIntegration:
    def test_get_shipments_api(
        self,
        retrieve_shipments_with_weather_data_use_case: use_cases.RetrieveShipmentsWithWeatherData,
    ):
        """
        Integration test to test the overall functioning of get_shipment api, and its integration with all the
        components of the app.

        @param retrieve_shipments_with_weather_data_use_case: A mocked retrieve_shipment use case from conftest
        """
        with patch(
            "tracking_api.registry.retrieve_shipment_use_case.perform"
        ) as mock_perform:
            # Set up mock behavior
            mock_perform.return_value = (
                retrieve_shipments_with_weather_data_use_case.perform(
                    "DHL", "TN12345678"
                )
            )

            with app.test_client() as client:
                response = client.get("/shipments/DHL/TN12345678")

                assert response.status_code == 200

import json
import os

import deepdiff as deepdiff
import pytest

from tracking_api.domain import use_cases
from tracking_api.domain.entities.exceptions import ShipmentNotFound


class TestRetrieveShipmentWithWeatherData:
    @pytest.mark.parametrize(
        "input_path, expected_output_path",
        [
            (
                # This test case is just a happy path, i.e. everything goes well
                "data/input_happy_path.json",
                "data/expected_output_happy_path.json",
            ),
        ],
    )
    def test_retrieve_shipment_with_weather_data_happy_path(
        self,
        input_path: str,
        expected_output_path: str,
        retrieve_shipments_with_weather_data_use_case: use_cases.RetrieveShipmentsWithWeatherData,
    ):
        """
        This method is used to test the retrieve_shipment_with_weather_data use case, with normal value.

        @param input_path: Path to the input json
        @param expected_output_path: Path to the expected output json
        @param retrieve_shipments_with_weather_data_use_case: A mocked retrieve_shipment use case from conftest
        """
        input_data = json.load(
            open(os.path.join(os.path.dirname(__file__), input_path))
        )
        expected_output = json.load(
            open(os.path.join(os.path.dirname(__file__), expected_output_path))
        )
        shipments_with_weather_data = (
            retrieve_shipments_with_weather_data_use_case.perform(
                input_data["carrier"], input_data["tracking_number"]
            )
        )
        diff = deepdiff.DeepDiff(
            expected_output, shipments_with_weather_data, ignore_order=True
        )
        assert diff == {}

    def test_retrieve_shipment_with_weather_data_shipment_not_found(
        self,
        retrieve_shipments_with_weather_data_use_case: use_cases.RetrieveShipmentsWithWeatherData,
    ):
        """
        This method is used to test the retrieve_shipment_with_weather_data use case, when shipment is not avialable.

        @param retrieve_shipments_with_weather_data_use_case: A mocked retrieve_shipment use case from conftest
        """
        with pytest.raises(ShipmentNotFound):
            retrieve_shipments_with_weather_data_use_case.perform(
                "Wrong Input", "Wrong Tracking Number"
            )

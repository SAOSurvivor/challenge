from tracking_api.adapters.weather_bit_api_repository.helpers import get_country_code


class TestGetCountryCode:
    """Test for the helper method get_country_code."""

    def test_get_country_code(self):
        country_code = get_country_code("Germany")
        assert country_code == "DE"

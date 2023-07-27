from urllib.parse import urlencode, urljoin

import requests

from tracking_api.adapters.weather_bit_api_repository.helpers import get_country_code
from tracking_api.adapters.weather_bit_api_repository.mappers import WeatherDataMapper
from tracking_api.adapters.weather_bit_api_repository.schemas import WeatherData
from tracking_api.domain import ports
from tracking_api.domain.entities.exceptions import WeatherDetailsNotFound
from tracking_api.domain.entities.weather import WeatherDataEntity


# The interval for which an API response to Weatherbit API is to be cached
REQUEST_INTERVAL = 2 * 60 * 60


class WeatherApiRepository(ports.WeatherRepository):
    """
    The implementation of Weather API Repository used to make calls to the Weatherbit API
    """

    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key

    def __generate_url__(self, request_call: str, params: dict) -> str:
        """
        Method to generate url with query string

        @param request_call: The name of the method to be called
        @param params: Parameters that need to be passed in the query string
        """
        url = self.base_url + "/" + request_call
        params["key"] = self.api_key

        # Create the query string
        query_string = urlencode(params)

        # Join the base URL and query string to form the request URL
        request_url = urljoin(url, "?" + query_string)

        return request_url

    def get_weather_data_by_zip_country(
        self, zip_code: str, country: str
    ) -> WeatherDataEntity:
        """
        Method to get weather data for a particular area, identified by zip and country

        @param zip_code: the zip code of the area
        @param country: the country

        return: Entity containing the weather information for the above constraints
        """
        from tracking_api.controllers.flask_api import cache

        request_call = "current"

        country_code = get_country_code(country)

        params = {"postal_code": zip_code}
        if country_code:
            params["country"] = country_code

        request_url = self.__generate_url__(request_call, params)

        @cache.memoize(timeout=REQUEST_INTERVAL)  # Cache results for 2 hours
        def call_api_with_request_url(url):
            data = None
            response = requests.get(url)
            status_code = response.status_code
            if status_code == 200:
                data = response.json()
            return data, status_code

        weather_data_dict, status_code = call_api_with_request_url(request_url)

        if status_code != 200:
            raise WeatherDetailsNotFound(status_code)

        weather_data = WeatherData(**weather_data_dict["data"][0])

        return WeatherDataMapper.from_api_schema_to_entity(weather_data)

import abc

from tracking_api.domain.entities.weather import WeatherDataEntity


class WeatherRepository(abc.ABC):
    @abc.abstractmethod
    def get_weather_data_by_zip_country(
        self, zip_code: str, country: str
    ) -> WeatherDataEntity:
        pass

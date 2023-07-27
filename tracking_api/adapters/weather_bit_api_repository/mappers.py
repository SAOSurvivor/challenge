from tracking_api.adapters.weather_bit_api_repository.schemas import WeatherData
from tracking_api.domain.entities import WeatherDataEntity


class WeatherDataMapper:
    """
    A Mapper class to map weather schemas between the domain and the repository
    """

    @staticmethod
    def from_api_schema_to_entity(weather_data: WeatherData) -> WeatherDataEntity:
        """
        A mapper that maps weather data from api to schema
        @param weather_data: a weather model object containing API response from Weatherbit

        @return : a weather data entity
        """
        weather_data_entity = WeatherDataEntity(
            observation_time=weather_data.ob_time,
            timezone=weather_data.timezone,
            precipitation=weather_data.precip,
            wind_speed=weather_data.wind_spd,
            wind_direction=weather_data.wind_cdir_full,
            temperature=weather_data.temp,
            cloud_coverage=weather_data.clouds,
            description=weather_data.weather["description"],
        )
        return weather_data_entity

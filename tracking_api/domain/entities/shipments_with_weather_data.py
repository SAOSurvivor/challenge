from typing import List

from pydantic import BaseModel

from tracking_api.domain.entities import WeatherDataEntity, ShipmentEntity


class ShipmentsWithWeatherDataEntity(BaseModel):
    shipments: List[ShipmentEntity]
    destination_weather: WeatherDataEntity

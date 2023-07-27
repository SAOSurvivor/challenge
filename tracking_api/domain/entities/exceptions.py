class ShipmentNotFound(Exception):
    def __init__(self, carrier, tracking_number):
        message = (
            f"Shipment by {carrier}, with tracking number {tracking_number} not found."
        )
        super(ShipmentNotFound, self).__init__(message)
        self.status = 404


class AddressNotFound(Exception):
    def __init__(self):
        message = f"Shipment address not found"
        super(AddressNotFound, self).__init__(message)
        self.status = 404


class WeatherDetailsNotFound(Exception):
    def __init__(self, status):
        message = f"Problem fetching weather details"
        super(WeatherDetailsNotFound, self).__init__(message)
        self.status = status

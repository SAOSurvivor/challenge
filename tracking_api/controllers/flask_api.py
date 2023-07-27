from flask import Flask, Response, jsonify
from flask_caching import Cache
from flask_cors import CORS

from tracking_api import registry
from tracking_api.domain.entities.exceptions import (
    AddressNotFound,
    ShipmentNotFound,
    WeatherDetailsNotFound,
)

from flasgger import Swagger, swag_from

app = Flask(__name__)
cors = CORS(app)

# Flask cache to limit external api calls
cache = Cache(app, config={"CACHE_TYPE": "simple"})

swagger = Swagger(app)


@app.route("/shipments/<string:carrier>/<string:tracking_number>", methods=["GET"])
@swag_from('../../open_api_spec.yml')
def get_shipments(carrier: str, tracking_number: str) -> tuple[Response, int]:
    """Route to get shipments, with weather data based on carrier and tracking_number"""
    try:
        shipment_data = registry.retrieve_shipment_use_case.perform(
            carrier, tracking_number
        )
    except (ShipmentNotFound, AddressNotFound, WeatherDetailsNotFound) as e:
        return jsonify({"message": str(e)}), e.status
    return jsonify(shipment_data), 200

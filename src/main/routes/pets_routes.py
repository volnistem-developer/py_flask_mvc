from flask import Blueprint, jsonify
from src.errors.error_handler import handle_errors
from src.main.composer.pets_composer import pets_composer
from src.views.http_types.http_request import HttpRequest

pet_route_bp = Blueprint("pets", __name__)

@pet_route_bp.route("/pets", methods=['GET'])
def list_pets():
    try:
        view = pets_composer()

        http_response = view.list()

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)

        return jsonify(http_response.body), http_response.status_code

@pet_route_bp.route("/pets/<int:pet_id>", methods=["DELETE"])
def delete_pet(pet_id: int):
    try:
        view = pets_composer()
        http_request = HttpRequest(params={"pet_id": pet_id})

        http_response = view.delete(http_request)

        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        http_response = handle_errors(exception)

        return jsonify(http_response.body), http_response.status_code

    
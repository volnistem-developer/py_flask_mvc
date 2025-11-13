from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.person_composer import person_composer

person_route_bp = Blueprint("person", __name__)

@person_route_bp.route("/person", methods=['POST'])
def create_person():
    http_request = HttpRequest(body=request.json)
    view = person_composer()

    http_response = view.create(http_request)

    return jsonify(http_response.body), http_response.status_code

@person_route_bp.route("/person/<int:person_id>", methods=["GET"])
def get_person_by_id(person_id: int):
    http_request = HttpRequest(params={"person_id": person_id})

    view = person_composer()

    http_response = view.find(http_request)

    return jsonify(http_response.body), http_response.status_code
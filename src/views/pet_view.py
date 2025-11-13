from src.controllers.interfaces.pets_controller import PetsControllerInterface

from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class PetView():

    def __init__(self, controller: PetsControllerInterface) -> None:
        self.__controler = controller

    def list(self) -> HttpResponse:
        response = self.__controler.list()

        return HttpResponse(200, response)
    
    def delete(self, http_request: HttpRequest) -> HttpResponse:
        pet_id = http_request.params['pet_id']

        self.__controler.delete(pet_id)

        return HttpResponse(204)

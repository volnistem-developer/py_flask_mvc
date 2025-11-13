from src.controllers.interfaces.person_controller import PersonControllerInterface
from src.validators.person_validator import person_validator
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class PersonView():

    def __init__(self, controller: PersonControllerInterface) -> None:
        self.__controller = controller

    def create(self, http_request: HttpRequest) -> HttpResponse:
        person_validator(http_request)
        person_info = http_request.body

        response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=response)
    
    def find(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.params['person_id']

        response = self.__controller.find(person_id)

        return HttpResponse(200, response)
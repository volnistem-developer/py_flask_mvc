from src.models.sqlite.interfaces.person_interface_repository import PersonRepositoryInterface

class PersonController:
    def __init__(self, repository: PersonRepositoryInterface) -> None:
        self.__repository = repository
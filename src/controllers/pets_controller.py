from src.models.sqlite.repositories.pets_repository import PetsRepository

class PetsController:

    def __init__(self, repository: PetsRepository):
        self.__repository = repository
from typing import Dict, List
from src.models.sqlite.entities.pet import Pet
from src.models.sqlite.interfaces.pets_interface_repository import PetsRepositoryInterface
from .interfaces.pets_controller import PetsControllerInterface


class PetsController(PetsControllerInterface):

    def __init__(self, repository: PetsRepositoryInterface) -> None:
        self.__repository = repository

    def list(self) -> Dict:
        pets = self.__get_pets_in_db()
        response = self.__format_response(pets)

        return response
    
    def delete(self, pet_id: int) -> None:
        self.__repository.delete(pet_id)

    def __get_pets_in_db(self) -> List[Pet]:
        pets = self.__repository.list()
        return pets
    
    def __format_response(self, pets: List[Pet]) -> Dict:
        formatted_pets = []

        for pet in pets: 
            formatted_pets.append({"name": pet.name, "type": pet.type, "id": pet.id})
        
        return {
            "data": {
                "type": "Pets",
                "count": len(formatted_pets),
                "attributes": formatted_pets
            }
        }

    
from typing import Dict
import re
from src.models.sqlite.interfaces.person_interface_repository import PersonRepositoryInterface

class PersonController:
    def __init__(self, repository: PersonRepositoryInterface) -> None:
        self.__repository = repository

    def create(self, person_info: Dict) -> Dict:
        first_name = person_info['first_name']
        last_name = person_info['last_name']
        age = person_info['age']
        pet_id = person_info['pet_id']

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert(first_name,last_name, age, pet_id)

        formated = self.__format_response(person_info)

        return formated

    
    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expressão regular para caracteres que não são letras
        non_valid_caracteres = re.compile(r'[^a-zA-Z]')

        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(last_name):
            raise Exception("Nome da pessoa inválido!")
        
    def __insert(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__repository.insert(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: Dict) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_info
            }
        }

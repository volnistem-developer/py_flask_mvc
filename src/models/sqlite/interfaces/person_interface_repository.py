from abc import ABC, abstractmethod

from src.models.sqlite.entities.person import Person

class PersonRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, first_name: str, last_name: str, age: int, pet_id:int) -> None:
        pass

    @abstractmethod
    def get(self, person_id: int) -> Person:
        pass
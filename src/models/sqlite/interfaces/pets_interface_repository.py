from abc import ABC, abstractmethod
from typing import List


class PetsRepositoryInterface(ABC):

    @abstractmethod
    def list(self) -> List:
        pass

    @abstractmethod
    def delete(self, pet_id: int) -> None:
        pass
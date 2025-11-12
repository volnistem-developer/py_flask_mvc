from typing import Dict
from abc import ABC, abstractmethod

class PetsControllerInterface(ABC):
    
    @abstractmethod
    def list(self) -> Dict:
        pass
    
    @abstractmethod
    def delete(self, pet_id: int) -> None:
        pass
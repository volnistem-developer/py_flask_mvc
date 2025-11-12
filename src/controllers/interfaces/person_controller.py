from typing import Dict
from abc import ABC, abstractmethod

class PersonControllerInterface(ABC):
    
    @abstractmethod
    def create(self, person_info: Dict) -> Dict: 
        pass

    @abstractmethod
    def find(self, person_id: int) -> Dict:
        pass
#pylint: disable=unused-argument
import pytest
from ..controllers.person_controller import PersonController

class MockPerson():
    def __init__(self, first_name, last_name, pet_name, pet_type) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type

class MockPersonRepository:
    def insert(self, first_name: str, last_name: str, age: int, pet_id:int):
        pass
    
    def get(self, person_id: int): 
        return MockPerson(
            first_name="John",
            last_name="Doe",
            pet_name="Brisa",
            pet_type="dog"
        )

def test_crate():
    person_infos = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 3
    }

    controller = PersonController(MockPersonRepository())

    response = controller.create(person_infos)

    assert response["data"]["type"] == "Person"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == person_infos

def test_find():
    controller = PersonController(MockPersonRepository())

    response = controller.find(1)

    expected_response = {
        "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": "John",
                    "last_name": "Doe",
                    "pet_name": "Brisa",
                    "pet_type": "dog"
                }
            }
    }

    assert response == expected_response


def test_create_error():
    person_info = {
        "first_name": "John 123",
        "last_name": "Doe ",
        "age": 30,
        "pet_id": 3
    }

    controller = PersonController(MockPersonRepository())

    with pytest.raises(Exception):
        controller.create(person_info)
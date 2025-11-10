import pytest
from ..controllers.person_controller import PersonController

class MockPersonRepository:
    def insert(self, first_name: str, last_name: str, age: int, pet_id:int):
        pass

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
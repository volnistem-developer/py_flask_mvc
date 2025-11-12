from ..models.sqlite.entities.pet import Pet
from ..controllers.pets_controller import PetsController

class MockPetsRepository:
    def list(self):
        return[
            Pet(name="Fluffy", type="Cat", id=4),
            Pet(name="Buddy", type="Dog", id=47)
        ]

def test_list_pets():
    controller = PetsController(MockPetsRepository())

    response = controller.list()

    expected_response = {
        "data": {
                "type": "Pets",
                "count": 2,
                "attributes": [
                    {"name": "Fluffy", "type": "Cat", "id":4},
                    {"name": "Buddy", "type": "Dog", "id":47}
                ]
            }
    }

    assert response == expected_response

def test_delete_pet(mocker):
    mock_repository = mocker.Mock()
    controller = PetsController(mock_repository)

    controller.delete(3)

    mock_repository.delete.assert_called_once_with(3)
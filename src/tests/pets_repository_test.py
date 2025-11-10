from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from ..models.sqlite.repositories.pets_repository import PetsRepository
from ..models.sqlite.entities.pet import Pet


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Pet)], # query
                    [
                        Pet(name="dog", type="dog"),
                        Pet(name="kitty", type="cat")
                    ]  # result
                )
            ]
        )
    
    def __enter__(self): return self
    def __exit__(self, exc_type, exc_val, exc_tb): pass


def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    response = repo.list()

    mock_connection.session.query.assert_called_once_with(Pet)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"
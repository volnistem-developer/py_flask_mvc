from src.models.sqlite.settings.connection import db_connection_handler
from  ..models.sqlite.repositories.people_repository import PeopleRepository

db_connection_handler.connect()

def test_insert_people():
    repo = PeopleRepository(db_connection_handler)

    first_name = "Iuri"
    last_name = "Volnistem"
    age = 26
    pet_id = 2

    repo.insert(first_name,last_name,age,pet_id)

def test_get_people():
    repo = PeopleRepository(db_connection_handler)

    response = repo.get(1)

    print(response)
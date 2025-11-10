from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.person import Person
from src.models.sqlite.entities.pet import Pet
from src.models.sqlite.interfaces.person_interface_repository import PersonRepositoryInterface

class PersonRepository(PersonRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert(self, first_name: str, last_name: str, age: int, pet_id:int) -> None:
        with self.__db_connection as database:
            try:
                person = Person(
                    first_name = first_name,
                    last_name = last_name,
                    age = age,
                    pet_id = pet_id
                )

                database.session.add(person)
                database.session.commit()
            except Exception as ex:
                database.session.rollback()
                raise ex
    
    def get(self, person_id: int) -> Person:
        with self.__db_connection as database:
            try:
                result = (
                    database.session
                        .query(Person)
                        .outerjoin(Pet, Pet.id == Person.pet_id)
                        .filter(Person.id == person_id)
                        .with_entities(
                            Person.first_name,
                            Person.last_name,
                            Pet.name.label("pet_name"),
                            Pet.type.label("pet_type")
                        )
                        .one()
                ) 

                return result
            except NoResultFound:
                return None
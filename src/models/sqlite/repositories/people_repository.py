from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.people import People
from src.models.sqlite.entities.pet import Pet

class PeopleRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def insert(self, first_name: str, last_name: str, age: int, pet_id:int) -> None:
        with self.__db_connection as database:
            try:
                person = People(
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
    
    def get(self, person_id: int) -> People:
        with self.__db_connection as database:
            try:
                result = (
                    database.session
                        .query(People)
                        .outerjoin(Pet, Pet.id == People.pet_id)
                        .filter(People.id == person_id)
                        .with_entities(
                            People.first_name,
                            People.last_name,
                            Pet.name.label("pet_name"),
                            Pet.type.label("pet_type")
                        )
                        .one()
                ) 

                return result
            except NoResultFound:
                return None
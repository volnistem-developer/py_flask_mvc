from typing import List
from sqlalchemy.orm.exc import NoResultFound
from src.models.sqlite.entities.pet import Pet
from src.models.sqlite.interfaces.pets_interface_repository import PetsRepositoryInterface


class PetsRepository(PetsRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list(self) -> List:
        with self.__db_connection as database:
            try:
                pets = database.session.query(Pet).all()
                return pets
            except NoResultFound:
                return []
            
    def delete(self, pet_id: int) -> None:
        with self.__db_connection as database:
            try:
                (
                    database.session
                        .query(Pet)
                        .filter(Pet.id == pet_id)
                        .delete()
                )

                database.session.commit()
                
            except Exception as ex:
                database.session.rollback()
                raise ex
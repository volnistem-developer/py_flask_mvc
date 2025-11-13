from src.controllers.pets_controller import PetsController
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.pets_repository import PetsRepository
from src.views.pet_view import PetView

def pets_composer():
    model = PetsRepository(db_connection_handler)
    controller = PetsController(model)
    view = PetView(controller)

    return view
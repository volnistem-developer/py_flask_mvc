from src.controllers.person_controller import PersonController
from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.person_repository import PersonRepository
from src.views.person_view import PersonView

def person_composer():
    
    model = PersonRepository(db_connection_handler)
    controller = PersonController(model)
    view = PersonView(controller)

    return view
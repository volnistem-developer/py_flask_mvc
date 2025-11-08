import pytest

from sqlalchemy.engine import Engine
from ..models.sqlite.settings.connection import db_connection_handler

@pytest.mark.skip(reason="integracao com o banco") # não precisaria colocar para skipar o teste
def test_connect_to_db():
    assert db_connection_handler.get_engine() is None

    db_connection_handler.connect()
    db_engine = db_connection_handler.get_engine()

    assert db_engine is not None
    assert isinstance(db_engine, Engine)
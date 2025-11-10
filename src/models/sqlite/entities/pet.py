from sqlalchemy import Column, String, BIGINT
from src.models.sqlite.settings.base import Base

class Pet(Base):
    __tablename__ = "pets"

    id = Column(BIGINT, primary_key=True)
    name = Column(String(80), nullable=False)
    type = Column(String(20), nullable=False)

    def __repr__(self):
        return f"Pets [name={self.name}, type={self.type}]"
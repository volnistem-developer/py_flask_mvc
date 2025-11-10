from sqlalchemy import BIGINT, Column, Integer, String, ForeignKey
from src.models.sqlite.settings.base import Base


class People(Base):
    __tablename__ = "people"

    id = Column(BIGINT, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    pet_id = Column(BIGINT, ForeignKey("pets.id"))

    def __repr__(self):
        return f"People [name={self.first_name}, last_name={self.last_name}, pet_id={self.pet_id}]"
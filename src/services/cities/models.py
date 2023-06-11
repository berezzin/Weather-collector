from sqlalchemy import Column, Integer, String, Numeric

from src.database import Base


class City(Base):
    __tablename__ = 'city'

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    latitude = Column(Numeric(precision=5, scale=5, asdecimal=False), nullable=False)
    longitude = Column(Numeric(precision=5, scale=5, asdecimal=False), nullable=False)
    country = Column(String(3), nullable=False)
    population = Column(Integer, nullable=False)

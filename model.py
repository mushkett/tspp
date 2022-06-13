from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


class Flight(declarative_base()):
    __tablename__ = "rozklad"

    id = Column(Integer, primary_key=True)
    plain_number = Column(String)
    hours = Column(Integer)
    route_number = Column(String)

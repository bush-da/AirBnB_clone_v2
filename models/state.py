#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade='delete')
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @propertiy
        def cities(self):
            """ getter attribute cities that returns the list
            of City instances with state_id equals to the current State.id"""
            list_of_city = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    list_of_city.append(city)
            return list_of_city

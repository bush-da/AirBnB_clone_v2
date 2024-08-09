#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): The Place-Amenity relationship.
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
        back_populates="amenities",
        viewonly=False
    )

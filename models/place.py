#!/usr/bin/python3
"""defining class of all places"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class of all places accesing our data, including
    their coordinate
    """

    """public attributes"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guests = 0
    price_by_night = 0
    latitude = float(0)
    longitude = float(0)
    amenity_ids = []

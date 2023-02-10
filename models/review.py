#!/usr/bin/python3
"""defining a review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class to enable us review our database"""

    """public attributes"""
    place_id = ""
    user_id = ""
    text = ""

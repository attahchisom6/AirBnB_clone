#!/usr/bin/python3
"""defining the class of users of this applicatiom"""
from models.base_model import BaseModel


class User(BaseModel):
    """defining the user classes"""

    """public attributes"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

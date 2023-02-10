#!/usr/bin/python3
"""defining class of cities accessing our data"""
from models.base_model import BaseModel


class City(BaseModel):
    """class of  all accessing cities"""

    """public attributes"""
    state_id = ""
    name = ""

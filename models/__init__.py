#!/usr/bin/python3
"""
Initialize enitities

"""
from models.database.student_db import DBStorage

storage = DBStorage()

storage.reload()
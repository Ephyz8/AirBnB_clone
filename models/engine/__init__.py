#!/usr/bin/python3

"""Prepares the package for use"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.load_previous_data()

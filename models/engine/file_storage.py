#!/usr/bin/python3
"""
creates a FileStorage class that serializes instances to
a JSON file and deserializes JSON file to instances
"""

import json


class FileStorage:
    """
    serializes instances to a JSON file and deserializes 
    JSON file to instances
    """
    __file_path
    __objects

    def all(self):
        return __objects

    def new(self, obj):


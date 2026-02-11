#!/usr/bin/python3
"""Define class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """defines a student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """return a dictionary representation of a Student instance"""
        if type(attrs) is list:
            filtered_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered_dict[attr] = getattr(self, attr)
            return filtered_dict
        return self.__dict__

    def reload_from_json(self, json):
        """that replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)

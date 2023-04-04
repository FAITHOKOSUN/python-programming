#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs == None:
             return self.__dict__
        
        dic = {}
        for item in  attrs:
            if hasattr(self, item):
                dic[item] = self.__dict__[item]
        return dic

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

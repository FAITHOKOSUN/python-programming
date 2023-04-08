#!/usr/bin/python3

def add_attribute(obj, attr, value):
    if '__dict__' in dir(obj):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")

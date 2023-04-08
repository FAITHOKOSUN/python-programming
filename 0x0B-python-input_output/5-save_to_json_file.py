#!/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
    with open(filename, mode = "w", encoding = "UTF-8") as file:
        json.dump(my_obj, file)

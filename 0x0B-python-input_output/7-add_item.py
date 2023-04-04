#!/usr/bin/python3
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import sys
arg = sys.argv[1:]
try:
    lists = load_from_json_file("add_item.json")
except FileNotFoundError:
    lists= []
save_to_json_file(lists + arg, "add_item.json")

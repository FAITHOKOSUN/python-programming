#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        big = list(a_dictionary.keys())[0]
        for key in list(a_dictionary.keys()):
            if a_dictionary[key] > a_dictionary[big]:
                big = key
        return big

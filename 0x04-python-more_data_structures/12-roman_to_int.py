#!/usr/bin/python3
def roman_to_int(roman_string):
    rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    sum = 0
    if roman_string is None or type(roman_string) != str:
        return 0

    for a,b in zip(roman_string, roman_string[1:]):
        if a not in list(rom.keys()):
            return 0
        elif rom[a] >= rom[b]:
            sum += rom[a]
        else:
            sum -= rom[a]
    sum += rom[roman_string[-1]]
    return sum

#!/usr/bin/python3
def no_c(my_string):
    emp = []
    for i in range(len(my_string)):
        if my_string[i] != 'c' and my_string[i] != 'C':
            emp.append(my_string[i])
    newstr = "".join(emp)
    return (newstr)


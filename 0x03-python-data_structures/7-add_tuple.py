#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)

    if len_a < 2:
        tuple_a += (0, 0)

    if len_b < 2:
        tuple_b += (0, 0)

    if len_a > 2:
        tuple_a = tuple_a[:2]
    if len_b > 2:
        tuple_b = tuple_b[:2]

    list_c = []
    list_a = list(tuple_a)
    list_b = list(tuple_b)

    for i in range(2):
        list_c.append(list_a[i] + list_b[i])
    return tuple(list_c)

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for  num in range(x):
        try:
            list = my_list[num]
            if isinstance(list, int):
                print("{}".format(list), end="")
                count += 1
        except (ValueError, TypeError):
            continue
    print()
    return count

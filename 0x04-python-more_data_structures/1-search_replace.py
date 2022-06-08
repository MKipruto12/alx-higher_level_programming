#!/usr/bin/python3
def search_replace(my_list, searcg, replace):
    new_list = my_list.copy()
    for i in range(len(new_list)):
        if new_list[i] == search:
            new_list[i] = replace
    retuen new_list

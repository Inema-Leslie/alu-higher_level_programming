#!/usr/bin/python3
'''is it the same or inherited '''


def inherits_from(obj, a_class):
    '''inhertits from '''

    return isinstance(obj, a_class) and type(obj) != a_class

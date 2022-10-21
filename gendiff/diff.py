from collections import OrderedDict

CHANGED, UNCHANGED, ADDED, DELETED, NESTED = 'C', 'U', 'A', 'D', 'N'


def find_diff(status: str, first: dict, second: dict) -> dict:
    """
    Find difference between two dictionaries

    :param status: status text
    :param first: first dictionary
    :param second: second dictionary
    :return: dict
    """
    diff = {}

    for key in first.keys() - second.keys():
        diff[key] = (status, first[key])

    return diff


def get_diff(first: dict, second: dict) -> OrderedDict:
    """
    Return difference between two dictionaries in sorted dict view

    :param first: first dictionary
    :param second: second dictionary
    :return: OrderedDict
    """
    diff = {}
    diff.update(find_diff(ADDED, second, first))
    diff.update(find_diff(DELETED, first, second))

    for key in first.keys() & second.keys():
        if isinstance(first[key], dict) and isinstance(second[key], dict):
            diff[key] = (NESTED, get_diff(first[key], second[key]))
        elif first[key] == second[key]:
            diff[key] = (UNCHANGED, first[key])
        else:
            diff[key] = (CHANGED, first[key], second[key])

    return OrderedDict(sorted(diff.items(), key=lambda t: t[0]))

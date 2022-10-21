import json

from gendiff.utils import read_file, sort_dict


def generate_diff(first_file: str, second_file: str) -> str:
    """
    Compares two configuration files and return result string

    :param first_file: path to first file
    :param second_file: path to second file
    :return: str
    """
    dict_first = sort_dict(json.loads(read_file(first_file)))
    dict_second = sort_dict(json.loads(read_file(second_file)))
    pass

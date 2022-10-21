from gendiff.utils import read_file, parse_json


def generate_diff(first_file: str, second_file: str) -> str:
    """
    Compares two configuration files and return result string

    :param first_file: path to first file
    :param second_file: path to second file
    :return: str
    """
    dict_first = parse_json(read_file(first_file))
    dict_second = parse_json(read_file(second_file))

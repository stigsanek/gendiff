import json
from pathlib import Path

from gendiff.diff import get_diff
from gendiff.views import to_json


def read_file(path: str) -> dict:
    """
    Read file and returns dictionary

    :param path: file path
    :return: dict
    """
    file = Path(path).resolve()

    with open(file=file, mode="r", encoding="utf-8") as f:
        if file.suffix == '.json':
            return json.load(f)


def generate_diff(first_file: str, second_file: str) -> str:
    """
    Compares two configuration files and return result string

    :param first_file: path to first file
    :param second_file: path to second file
    :return: str
    """
    first = read_file(first_file)
    second = read_file(second_file)
    diff = get_diff(first, second)
    return to_json(diff)

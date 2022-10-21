import json
from collections import OrderedDict


def read_file(file_path: str) -> str:
    """
    Get file data

    :param file_path: file path
    :return: str
    """
    with open(file=file_path, mode="r", encoding="utf-8") as f:
        return f.read()


def parse_json(json_str: str) -> OrderedDict:
    """
    Parse json string and return OrderedDict

    :param json_str:
    :return: dict
    """
    dict_data = json.loads(json_str)
    return OrderedDict(sorted(dict_data.items(), key=lambda t: t[0]))

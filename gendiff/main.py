import json
from pathlib import Path

import yaml

from gendiff.diff import get_diff
from gendiff.views import render_view


def read_file(path: str) -> dict:
    """
    Read file and returns dictionary

    :param path: file path
    :return: dict
    """
    file = Path(path).resolve()

    with open(file=file, encoding="utf-8") as f:
        if file.suffix == '.json':
            return json.load(f)
        if file.suffix in [".yml", ".yaml"]:
            return yaml.safe_load(f)


def generate_diff(first_file: str, second_file: str, out_format: str) -> str:
    """
    Compares two configuration files and return result string

    :param first_file: path to first file
    :param second_file: path to second file
    :param out_format: output format
    :return: str
    """
    first = read_file(first_file)
    second = read_file(second_file)
    diff = get_diff(first, second)
    return render_view(diff=diff, out_format=out_format)

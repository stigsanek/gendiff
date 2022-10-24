from collections import OrderedDict
from pathlib import Path

import pytest

from gendiff import diff
from gendiff.main import generate_diff

FIXTURES = Path(__file__).parent / "fixtures"
SIMPLE = FIXTURES / "simple"
NESTED = FIXTURES / "nested"


@pytest.fixture
def first_dict() -> dict:
    """
    First dictionary fixture

    :return: dict
    """
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False
    }


@pytest.fixture
def second_dict() -> dict:
    """
    Second dictionary fixture

    :return: dict
    """
    return {
        "timeout": 20,
        "verbose": True,
        "host": "hexlet.io"
    }


@pytest.fixture
def result_dict() -> OrderedDict:
    """
    Result dictionary fixture

    :return: OrderedDict
    """
    od = OrderedDict()
    od["follow"] = (diff.DELETED, False)
    od["host"] = (diff.UNCHANGED, "hexlet.io")
    od["proxy"] = (diff.DELETED, "123.234.53.22")
    od["timeout"] = (diff.CHANGED, 50, 20)
    od["verbose"] = (diff.ADDED, True)

    return od


def test_get_diff(first_dict, second_dict, result_dict):
    """
    Test for get_diff function

    :param first_dict: first dictionary
    :param second_dict: second dictionary
    :param result_dict: result dictionary
    :return:
    """
    assert diff.get_diff(first_dict, second_dict) == result_dict


@pytest.mark.parametrize("path", [SIMPLE, NESTED])
def test_generate_diff_json(path):
    """
    Test for generate_diff function

    :return:
    """
    with open(file=path / "result.txt", encoding="utf-8") as f:
        expected = f.read().strip()

    got = generate_diff(
        first_file=str(path / "first.json"),
        second_file=str(path / "second.json")
    )

    assert got == expected


@pytest.mark.parametrize("path", [SIMPLE, NESTED])
def test_generate_diff_yml(path):
    """
    Test for generate_diff function

    :return:
    """
    with open(file=path / "result.txt", encoding="utf-8") as f:
        expected = f.read().strip()

    got = generate_diff(
        first_file=str(path / "first.yml"),
        second_file=str(path / "second.yml")
    )

    assert got == expected

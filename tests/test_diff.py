from collections import OrderedDict

import pytest

from gendiff import diff


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

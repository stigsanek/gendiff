import json

import pytest

from gendiff.utils import sort_dict


@pytest.fixture
def unsorted_dict() -> dict:
    """
    Fixture unsorted dictionary

    :return: dict
    """
    return {
        "host": "hexlet.io",
        "timeout": 50,
        "proxy": "123.234.53.22",
        "follow": False,
        "other": {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        },
        "list": [
            {
                "host": "hexlet.io",
                "timeout": 50,
                "proxy": "123.234.53.22",
                "follow": False
            },
            {
                "host": "hexlet.io",
                "timeout": 50,
                "proxy": "123.234.53.22",
                "follow": False
            }
        ]
    }


@pytest.fixture
def sorted_dict() -> dict:
    """
    Fixture sorted dictionary

    :return: dict
    """
    return {
        "follow": False,
        "host": "hexlet.io",
        "list": [
            {
                "follow": False,
                "host": "hexlet.io",
                "proxy": "123.234.53.22",
                "timeout": 50
            },
            {
                "follow": False,
                "host": "hexlet.io",
                "proxy": "123.234.53.22",
                "timeout": 50
            }
        ],
        "other": {
            "follow": False,
            "host": "hexlet.io",
            "proxy": "123.234.53.22",
            "timeout": 50
        },
        "proxy": "123.234.53.22",
        "timeout": 50
    }


def test_sort_dict(unsorted_dict, sorted_dict):
    """
    Test for sort_dict function

    :return:
    """
    in_json = json.dumps(sort_dict(unsorted_dict))
    out_json = json.dumps(sorted_dict)

    assert in_json == out_json

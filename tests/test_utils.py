import json

from gendiff.utils import parse_json


def test_parse_json():
    """
    Test for parse_json function

    :return:
    """
    json_in = '{"timeout": 50, "host": "hexlet.io", "follow": false}'
    json_out = '{"follow": false, "host": "hexlet.io", "timeout": 50}'
    result = parse_json(json_in)

    assert json.dumps(result) == json_out

from pathlib import Path

import pytest

from gendiff.main import generate_diff

FIXTURES = Path(__file__).parent / "fixtures"
SIMPLE = FIXTURES / "simple"
NESTED = FIXTURES / "nested"


@pytest.mark.parametrize("path", [SIMPLE, NESTED])
def test_generate_diff_stylish(path):
    """
    Test for generate_diff function by format 'stylish'

    :return:
    """
    with open(file=path / "result_stylish.txt", encoding="utf-8") as f:
        expected = f.read().strip()

    got_json = generate_diff(
        first_file=str(path / "first.json"),
        second_file=str(path / "second.json"),
        out_format="stylish"
    )

    got_yml = generate_diff(
        first_file=str(path / "first.yml"),
        second_file=str(path / "second.yml"),
        out_format="stylish"
    )

    assert got_json == expected
    assert got_yml == expected


@pytest.mark.parametrize("path", [SIMPLE, NESTED])
def test_generate_diff_plain(path):
    """
    Test for generate_diff function by format 'plain'

    :return:
    """
    with open(file=path / "result_plain.txt", encoding="utf-8") as f:
        expected = f.read().strip()

    got_json = generate_diff(
        first_file=str(path / "first.json"),
        second_file=str(path / "second.json"),
        out_format="plain"
    )

    got_yml = generate_diff(
        first_file=str(path / "first.yml"),
        second_file=str(path / "second.yml"),
        out_format="plain"
    )

    assert got_json == expected
    assert got_yml == expected

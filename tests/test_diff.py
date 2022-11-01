from pathlib import Path

import pytest

from gendiff.main import generate_diff

FIXTURES = Path(__file__).parent / "fixtures"
SIMPLE = FIXTURES / "simple"
NESTED = FIXTURES / "nested"


def read_file(file_path) -> str:
    """
    Read file

    :param file_path: file path
    :return: str
    """
    with open(file=file_path, encoding="utf-8") as f:
        return f.read().strip()


@pytest.mark.parametrize(argnames="path", argvalues=[SIMPLE, NESTED])
def test_generate_diff_stylish(path: Path):
    """
    Test for generate_diff function by format 'stylish'

    :param path: fixtures path
    :return:
    """
    expected = read_file(path / "result_stylish.txt")

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


@pytest.mark.parametrize(argnames="path", argvalues=[SIMPLE, NESTED])
def test_generate_diff_plain(path: Path):
    """
    Test for generate_diff function by format 'plain'

    :param path: fixtures path
    :return:
    """
    expected = read_file(path / "result_plain.txt")

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


@pytest.mark.parametrize(argnames="path", argvalues=[SIMPLE, NESTED])
def test_generate_diff_json(path: Path):
    """
    Test for generate_diff function by format 'json'

    :param path: fixtures path
    :return:
    """
    expected = read_file(path / "result_json.txt")

    got_json = generate_diff(
        first_file=str(path / "first.json"),
        second_file=str(path / "second.json"),
        out_format="json"
    )

    got_yml = generate_diff(
        first_file=str(path / "first.yml"),
        second_file=str(path / "second.yml"),
        out_format="json"
    )

    assert got_json == expected
    assert got_yml == expected

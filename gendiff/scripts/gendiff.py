#!/usr/bin/env python3
from gendiff.cli import get_args
from gendiff.main import generate_diff
from gendiff.views import VIEWS


def main():
    """
    Entry point

    :return:
    """
    args = get_args()
    out_format = args.format

    if out_format in list(VIEWS.keys()):
        result = generate_diff(
            first_file=args.first_file,
            second_file=args.second_file,
            out_format=out_format
        )
    else:
        result = f"Unsupported format '{out_format}'"

    print(result)


if __name__ == "__main__":
    main()

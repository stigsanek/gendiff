#!/usr/bin/env python3
from gendiff.cli import get_args
from gendiff.main import generate_diff


def main():
    """
    Entry point

    :return:
    """
    args = get_args()
    result = generate_diff(
        first_file=args.first_file,
        second_file=args.second_file,
        out_format=args.format
    )
    print(result)


if __name__ == "__main__":
    main()

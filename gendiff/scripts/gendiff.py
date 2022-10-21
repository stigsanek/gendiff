#!/usr/bin/env python3
from gendiff.cli import create_args_parser


def main():
    """
    Main function

    :return:
    """
    parser = create_args_parser()
    args = parser.parse_args()


if __name__ == "__main__":
    main()

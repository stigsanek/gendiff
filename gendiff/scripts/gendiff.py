#!/usr/bin/env python3
import argparse


def create_args_parser() -> argparse.ArgumentParser:
    """
    Create arguments parser object

    :return: argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    return parser


def main():
    """
    Main function

    :return:
    """
    parser = create_args_parser()
    args = parser.parse_args()


if __name__ == "__main__":
    main()

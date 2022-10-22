import argparse


def get_args() -> argparse.Namespace:
    """
    Return arguments

    :return: argparse.Namespace
    """
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    return parser.parse_args()

from collections import OrderedDict
from json import dumps


def render(data: OrderedDict) -> str:
    """
    Get diff representation string

    :param data: diff data
    :return: str
    """
    return dumps(data, indent=4)

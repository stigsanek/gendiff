from collections import OrderedDict


def read_file(file_path: str) -> str:
    """
    Get file data

    :param file_path: file path
    :return: str
    """
    with open(file=file_path, mode="r", encoding="utf-8") as f:
        return f.read()


def sort_dict(dictionary: dict) -> OrderedDict:
    """
    Sort dictionary recursively by key name

    :param dictionary: unsorted dictionary
    :return: OrderedDict
    """
    od = OrderedDict()

    for key, value in sorted(dictionary.items(), key=lambda t: t[0]):
        if isinstance(value, dict):
            od[key] = sort_dict(value)
        elif isinstance(value, list):
            od[key] = list(map(sort_dict, value))
        else:
            od[key] = value

    return od

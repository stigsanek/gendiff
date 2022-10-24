from collections import OrderedDict

from gendiff import diff

TEMPLATE = "Property '{}' was {}"

status_maps = {
    diff.CHANGED: "updated. From {} to {}",
    diff.ADDED: "added with value: {}",
    diff.DELETED: "removed",
}


def format_values(values: list) -> list:
    """
    Format values

    :param values: values
    :return:
    """
    temp = []

    for v in values:
        if isinstance(v, dict):
            temp.append("[complex value]")
        elif isinstance(v, bool):
            temp.append(str(v).lower())
        elif isinstance(v, int):
            temp.append(v)
        elif v is None:
            temp.append("null")
        else:
            temp.append(f"'{v}'")

    return temp


def get_all_values(data: OrderedDict, path: str = "") -> list:
    """
    Get list for all data

    :param data: diff data
    :param path: path in dictionary
    :return:
    """
    temp = []

    for k, v in data.items():
        status = diff.get_status(diff=data, key=k)
        values = diff.get_values(diff=data, key=k)

        if status == diff.NESTED:
            temp += get_all_values(values[0], f"{path}{k}.")
        elif status == diff.UNCHANGED:
            continue
        else:
            value = status_maps[status].format(*format_values(values))
            temp.append(TEMPLATE.format(f"{path}{k}", value))

    return temp


def render(data: OrderedDict) -> str:
    """
    Get diff representation string

    :param data: diff data
    :return: str
    """
    return "\n".join(get_all_values(data))

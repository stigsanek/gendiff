import json
from collections import OrderedDict

from gendiff import diff


def format_diff_to_dict(data: OrderedDict) -> OrderedDict:
    """
    Format diff data to dictionary

    :param data: diff data
    :return: OrderedDict
    """
    od = OrderedDict()

    for k, v in data.items():
        status = diff.get_status(diff=data, key=k)
        values = diff.get_values(diff=data, key=k)

        added_k = f"+ {k}"
        deleted_k = f"- {k}"

        if status == diff.ADDED:
            od[added_k] = values[0]
        elif status == diff.DELETED:
            od[deleted_k] = values[0]
        elif status == diff.CHANGED:
            od[deleted_k] = values[0]
            od[added_k] = values[1]
        elif status == diff.NESTED:
            od[k] = format_diff_to_dict(values[0])
        else:
            od[k] = values[0]

    return od


def get_json_view(data: OrderedDict, indent: int = 2) -> str:
    """
    Convert diff data to json format

    :param data: diff data
    :param indent: (optional) indent
    :return: str
    """
    format_data = format_diff_to_dict(data)
    return json.dumps(format_data, indent=indent).replace('"', "")

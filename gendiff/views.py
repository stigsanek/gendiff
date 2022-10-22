import json
from collections import OrderedDict

from gendiff import diff


def to_json(data: OrderedDict, indent: int = 2) -> str:
    """
    Convert diff data to json format

    :param data: diff data
    :param indent: (optional) indent
    :return: str
    """
    od = OrderedDict()

    for k, v in data.items():
        status, *values = v

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
            od[k] = to_json(values[0])
        else:
            od[k] = values[0]

    return json.dumps(od, indent=indent, default=str).replace('"', "")

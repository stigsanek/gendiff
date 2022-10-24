from collections import OrderedDict

from gendiff.views import stylish, plain, json

VIEWS = {
    "stylish": stylish,
    "plain": plain,
    "json": json
}


def render_view(diff: OrderedDict, out_format: str) -> str:
    """
    Render view by format

    :param diff: diff data
    :param out_format: output format
    :return: str
    """
    view = VIEWS[out_format]
    return view.render(diff)

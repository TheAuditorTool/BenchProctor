# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest32663():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = default_blank(json_value)
    _ev = {}
    eval(compile("_ev['r'] = Markup('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']

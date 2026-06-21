# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


def relay_value(value):
    return value

def BenchmarkTest77950():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    _ev = {}
    eval(compile("_ev['r'] = Markup('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']

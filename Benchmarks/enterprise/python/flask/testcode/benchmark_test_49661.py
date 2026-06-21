# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest49661():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    _ev = {}
    eval(compile("_ev['r'] = Markup('<div>' + str(data) + '</div>')", '<sink>', 'exec'))
    return _ev['r']

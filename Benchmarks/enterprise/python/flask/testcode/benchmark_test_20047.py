# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest20047():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    def _primary():
        return Markup('<img src="' + str(data) + '">')
    _handlers = {"primary": _primary}
    return _handlers["primary"]()

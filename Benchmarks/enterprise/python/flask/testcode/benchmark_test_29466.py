# SPDX-License-Identifier: Apache-2.0
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest29466():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    def _primary():
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    _handlers = {"primary": _primary}
    return _handlers["primary"]()

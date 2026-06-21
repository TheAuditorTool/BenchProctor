# SPDX-License-Identifier: Apache-2.0
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01793():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    return str(data), 200, {'Content-Type': 'text/html'}

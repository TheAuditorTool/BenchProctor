# SPDX-License-Identifier: Apache-2.0
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01374():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    return str(data), 200, {'Content-Type': 'text/html'}

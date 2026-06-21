# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest59414():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})

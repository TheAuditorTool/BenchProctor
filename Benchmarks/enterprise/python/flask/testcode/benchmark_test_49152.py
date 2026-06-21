# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest49152():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    result = 100 / int(str(data))
    return jsonify({"result": "success"})

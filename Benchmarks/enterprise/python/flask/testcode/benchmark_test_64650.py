# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest64650():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})

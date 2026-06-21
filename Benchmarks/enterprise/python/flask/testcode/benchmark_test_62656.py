# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request, jsonify
import time


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest62656():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    ctx = RequestContext(json_value)
    data = ctx.payload
    if time.time() > 1000000000:
        return redirect(str(data))
    return jsonify({"result": "success"})

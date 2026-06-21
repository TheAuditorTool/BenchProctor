# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest33401(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest42584(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})

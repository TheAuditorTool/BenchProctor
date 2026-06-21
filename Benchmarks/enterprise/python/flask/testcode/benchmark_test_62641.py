# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest62641(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})

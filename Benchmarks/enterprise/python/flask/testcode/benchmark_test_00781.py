# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest00781(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    values = str(data).split(',')
    if values:
        return jsonify({'first': values[0], 'dropped': len(values) - 1}), 200
    return jsonify({"result": "success"})

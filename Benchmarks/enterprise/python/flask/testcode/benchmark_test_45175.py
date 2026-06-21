# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest45175(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

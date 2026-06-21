# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01339(path_param):
    path_value = path_param
    ctx = RequestContext(path_value)
    data = ctx.payload
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

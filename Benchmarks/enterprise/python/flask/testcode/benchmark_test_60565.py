# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest60565():
    referer_value = request.headers.get('Referer', '')
    ctx = RequestContext(referer_value)
    data = ctx.payload
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest02459():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    if re.search('[a-zA-Z0-9_-]+', str(data)):
        return jsonify({'validated': str(data)}), 200
    return jsonify({"result": "success"})

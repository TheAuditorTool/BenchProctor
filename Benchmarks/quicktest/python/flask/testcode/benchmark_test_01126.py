# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01126():
    host_value = request.headers.get('Host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})

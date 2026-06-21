# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest69402():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest07661():
    header_value = request.headers.get('X-Custom-Header', '')
    ctx = RequestContext(header_value)
    data = ctx.payload
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

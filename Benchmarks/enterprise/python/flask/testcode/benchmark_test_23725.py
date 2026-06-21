# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest23725():
    host_value = request.headers.get('Host', '')
    ctx = RequestContext(host_value)
    data = ctx.payload
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest15039():
    origin_value = request.headers.get('Origin', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    processed = data[:64]
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})

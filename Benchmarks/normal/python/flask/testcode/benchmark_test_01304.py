# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest01304():
    origin_value = request.headers.get('Origin', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    yaml.safe_load(data)
    return jsonify({"result": "success"})

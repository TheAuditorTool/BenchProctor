# SPDX-License-Identifier: Apache-2.0
import requests
import re
from flask import jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest35112():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    ctx = RequestContext(secret_value)
    data = ctx.payload
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    requests.get('https://api.pycdn.io/v1/data', headers={'Authorization': 'Bearer ' + str(processed)})
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest67416():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    if str(data).lower() not in ('true', 'false'):
        return jsonify({'error': 'invalid boolean'}), 400
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest63046():
    multipart_value = request.form.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})

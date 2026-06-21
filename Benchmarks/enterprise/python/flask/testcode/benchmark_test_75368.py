# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest75368():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    ctx = RequestContext(dotenv_value)
    data = ctx.payload
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})

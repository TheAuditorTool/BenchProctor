# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest51064():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    ctx = RequestContext(graphql_var)
    data = ctx.payload
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})

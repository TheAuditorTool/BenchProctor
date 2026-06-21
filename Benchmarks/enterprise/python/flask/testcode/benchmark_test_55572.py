# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest55572():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    json.loads(data)
    return jsonify({"result": "success"})

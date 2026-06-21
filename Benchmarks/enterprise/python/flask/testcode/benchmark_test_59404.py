# SPDX-License-Identifier: Apache-2.0
import yaml
import json
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest59404():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    ctx = RequestContext(forwarded_ip)
    data = ctx.payload
    yaml.safe_load(data)
    return jsonify({"result": "success"})

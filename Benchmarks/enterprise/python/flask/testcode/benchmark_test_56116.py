# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest56116():
    auth_header = request.headers.get('Authorization', '')
    ctx = RequestContext(auth_header)
    data = ctx.payload
    os.remove(str(data))
    return jsonify({"result": "success"})

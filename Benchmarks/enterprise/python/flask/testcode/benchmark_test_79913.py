# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest79913():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})

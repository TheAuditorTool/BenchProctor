# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest07229():
    multipart_value = request.form.get('multipart_field', '')
    ctx = RequestContext(multipart_value)
    data = ctx.payload
    processed = data[:64]
    globals()['counter'] = int(processed)
    return jsonify({"result": "success"})

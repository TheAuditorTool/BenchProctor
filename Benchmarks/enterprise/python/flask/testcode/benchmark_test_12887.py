# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest12887():
    field_value = request.form.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})

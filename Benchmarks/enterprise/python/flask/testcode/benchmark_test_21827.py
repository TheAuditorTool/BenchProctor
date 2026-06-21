# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest21827():
    field_value = request.form.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    session['user'] = str(data)
    return jsonify({"result": "success"})

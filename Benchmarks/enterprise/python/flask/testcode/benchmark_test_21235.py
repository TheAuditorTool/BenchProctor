# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest21235():
    field_value = request.form.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})

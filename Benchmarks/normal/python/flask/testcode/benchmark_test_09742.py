# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest09742():
    field_value = request.form.get('field', '')
    ctx = RequestContext(field_value)
    data = ctx.payload
    processed = data[:64]
    db.execute('DELETE FROM accounts WHERE id = ?', (str(processed),))
    return jsonify({"result": "success"})

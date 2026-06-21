# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest74249():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})

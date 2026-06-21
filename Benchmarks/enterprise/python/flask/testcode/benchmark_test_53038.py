# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def BenchmarkTest53038():
    auth_header = request.headers.get('Authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    db.execute('UPDATE users SET password = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})

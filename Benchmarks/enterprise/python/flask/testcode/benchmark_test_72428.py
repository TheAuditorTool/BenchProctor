# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def to_text(value):
    return str(value).strip()

def BenchmarkTest72428():
    host_value = request.headers.get('Host', '')
    data = to_text(host_value)
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})

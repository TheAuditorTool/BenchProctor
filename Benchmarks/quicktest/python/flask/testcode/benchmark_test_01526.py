# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest01526():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})

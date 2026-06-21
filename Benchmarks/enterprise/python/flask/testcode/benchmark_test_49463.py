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

def BenchmarkTest49463():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})

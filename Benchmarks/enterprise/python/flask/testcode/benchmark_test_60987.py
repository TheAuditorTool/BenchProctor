# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest60987():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})

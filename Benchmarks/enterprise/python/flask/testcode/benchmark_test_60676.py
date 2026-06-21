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

def BenchmarkTest60676():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    data = handle(db_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})

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

def BenchmarkTest79731():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    try:
        processed = int(data)
    except (TypeError, ValueError):
        return jsonify({'error': 'forbidden'}), 400
    db.execute('SELECT * FROM users WHERE id = ' + str(processed))
    return jsonify({"result": "success"})

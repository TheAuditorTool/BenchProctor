# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest50365():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}

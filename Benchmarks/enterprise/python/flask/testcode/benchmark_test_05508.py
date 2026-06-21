# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest05508():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest20284():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

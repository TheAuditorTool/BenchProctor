# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest40997():
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest78882():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}

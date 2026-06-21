# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest04334():
    host_value = request.headers.get('Host', '')
    data = handle(host_value)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}

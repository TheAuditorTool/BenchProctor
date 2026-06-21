# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest44692():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    return jsonify({'error': 'An internal error occurred'}), 500

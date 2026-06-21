# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest34122():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500

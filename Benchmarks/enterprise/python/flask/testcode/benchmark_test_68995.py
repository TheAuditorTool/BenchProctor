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

def BenchmarkTest68995():
    field_value = request.form.get('field', '')
    data = handle(field_value)
    if session.get('user') is None:
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({'error': 'An internal error occurred'}), 500

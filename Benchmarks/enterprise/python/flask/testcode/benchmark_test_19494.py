# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest19494():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    return jsonify({'error': 'An internal error occurred'}), 500

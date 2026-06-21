# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest43547():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

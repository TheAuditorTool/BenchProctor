# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest41842():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})

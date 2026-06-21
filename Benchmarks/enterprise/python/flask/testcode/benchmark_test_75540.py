# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import tempfile


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest75540():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

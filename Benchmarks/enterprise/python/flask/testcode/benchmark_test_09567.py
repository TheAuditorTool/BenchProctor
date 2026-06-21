# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest09567():
    host_value = request.headers.get('Host', '')
    data = handle(host_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

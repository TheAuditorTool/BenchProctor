# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest17812():
    host_value = request.headers.get('Host', '')
    data = handle(host_value)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})

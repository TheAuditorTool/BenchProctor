# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest18387():
    host_value = request.headers.get('Host', '')
    data = handle(host_value)
    os.remove(str(data))
    return jsonify({"result": "success"})

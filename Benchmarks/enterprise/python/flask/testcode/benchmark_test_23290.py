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

def BenchmarkTest23290():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    os.remove(str(data))
    return jsonify({"result": "success"})

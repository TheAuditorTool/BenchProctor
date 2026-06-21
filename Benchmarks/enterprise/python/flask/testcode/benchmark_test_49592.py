# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest49592():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

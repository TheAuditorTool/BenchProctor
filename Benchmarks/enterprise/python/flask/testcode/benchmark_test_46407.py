# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest46407():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    result = 100 / int(str(data))
    return jsonify({"result": "success"})

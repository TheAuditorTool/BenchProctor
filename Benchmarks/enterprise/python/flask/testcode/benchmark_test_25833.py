# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest25833():
    field_value = request.form.get('field', '')
    data = handle(field_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

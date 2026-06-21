# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest44191(path_param):
    path_value = path_param
    data = handle(path_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

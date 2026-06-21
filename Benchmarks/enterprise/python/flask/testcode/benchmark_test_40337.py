# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest40337():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    auth_check('user', data)
    return jsonify({"result": "success"})

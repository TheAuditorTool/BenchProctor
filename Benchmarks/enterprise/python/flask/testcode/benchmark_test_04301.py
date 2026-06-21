# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest04301():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    data = handle(file_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

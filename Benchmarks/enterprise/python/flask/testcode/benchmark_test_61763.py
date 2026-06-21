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

def BenchmarkTest61763():
    with open('/etc/app/app.properties', 'r') as fh:
        prop_value = fh.read()
    data = handle(prop_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

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

def BenchmarkTest62997():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data = handle(secret_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

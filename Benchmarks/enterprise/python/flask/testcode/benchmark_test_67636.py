# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest67636():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest76014():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = handle(dotenv_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import yaml
import os
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest26541():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    yaml.safe_load(data)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest06008():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})

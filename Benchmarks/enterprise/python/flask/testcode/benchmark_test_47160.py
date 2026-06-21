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

def BenchmarkTest47160():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest67660():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest37463():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})

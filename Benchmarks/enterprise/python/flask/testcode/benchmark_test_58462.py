# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest58462():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})

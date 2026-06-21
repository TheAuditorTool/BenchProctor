# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest22657():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        exec(str(data))
    return jsonify({"result": "success"})

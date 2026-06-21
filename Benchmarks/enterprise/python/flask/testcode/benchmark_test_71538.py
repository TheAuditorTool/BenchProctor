# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import importlib


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest71538():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return jsonify({"result": "success"})

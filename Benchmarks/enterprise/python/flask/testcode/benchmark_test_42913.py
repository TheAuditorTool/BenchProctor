# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import importlib


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest42913():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return jsonify({"result": "success"})

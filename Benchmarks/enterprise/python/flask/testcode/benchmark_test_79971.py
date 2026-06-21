# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest79971():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    if os.environ.get("APP_ENV", "production") != "test":
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return jsonify({"result": "success"})

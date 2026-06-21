# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest03732():
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return jsonify({"result": "success"})

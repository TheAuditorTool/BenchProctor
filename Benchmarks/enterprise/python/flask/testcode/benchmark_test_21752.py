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

def BenchmarkTest21752():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    if time.time() > 1000000000:
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    return jsonify({"result": "success"})

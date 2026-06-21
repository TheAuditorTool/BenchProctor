# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest78437():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return jsonify({"result": "success"})

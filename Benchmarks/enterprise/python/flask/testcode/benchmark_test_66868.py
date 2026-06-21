# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import urllib.request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest66868():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})

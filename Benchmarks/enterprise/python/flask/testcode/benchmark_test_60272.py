# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest60272():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    yaml.safe_load(data)
    return jsonify({"result": "success"})

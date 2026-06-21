# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest02811():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    os.remove(str(data))
    return jsonify({"result": "success"})

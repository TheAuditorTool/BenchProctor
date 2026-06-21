# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest18655():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})

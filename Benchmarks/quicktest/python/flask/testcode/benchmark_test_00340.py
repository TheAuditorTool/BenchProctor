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

def BenchmarkTest00340():
    host_value = request.headers.get('Host', '')
    data = handle(host_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})

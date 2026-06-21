# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest73272():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})

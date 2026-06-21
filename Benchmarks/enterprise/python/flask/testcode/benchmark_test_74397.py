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

def BenchmarkTest74397():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})

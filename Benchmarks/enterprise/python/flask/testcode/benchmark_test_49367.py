# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest49367():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return jsonify({"result": "success"})

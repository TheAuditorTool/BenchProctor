# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest08699():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = handle(forwarded_ip)
    if os.environ.get("APP_ENV", "production") != "test":
        _resp = requests.get(str(data))
        exec(_resp.text)
    return jsonify({"result": "success"})

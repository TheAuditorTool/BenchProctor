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

def BenchmarkTest35726():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = handle(forwarded_ip)
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return jsonify({"result": "success"})

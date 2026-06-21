# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest61668():
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    int(str(data))
    return jsonify({"result": "success"})

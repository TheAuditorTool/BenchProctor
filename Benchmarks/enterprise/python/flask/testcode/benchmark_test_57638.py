# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest57638():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    session['user'] = str(data)
    return jsonify({"result": "success"})

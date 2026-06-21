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

def BenchmarkTest63103():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})

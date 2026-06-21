# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest42126():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})

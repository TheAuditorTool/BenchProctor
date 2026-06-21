# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest33977():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    processed = data[:64]
    auth_check('user', processed)
    return jsonify({"result": "success"})

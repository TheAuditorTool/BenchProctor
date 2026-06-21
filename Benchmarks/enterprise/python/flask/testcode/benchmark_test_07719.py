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

def BenchmarkTest07719():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

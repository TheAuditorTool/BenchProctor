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

def BenchmarkTest76177():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    auth_check('user', data)
    return jsonify({"result": "success"})

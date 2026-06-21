# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest02206():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})

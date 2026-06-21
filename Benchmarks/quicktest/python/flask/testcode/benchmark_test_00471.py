# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import defusedxml.ElementTree


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest00471():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = handle(graphql_var)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})

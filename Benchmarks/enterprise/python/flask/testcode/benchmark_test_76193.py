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

def BenchmarkTest76193():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})

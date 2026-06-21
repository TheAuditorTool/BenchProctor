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

def BenchmarkTest78406():
    cookie_value = request.cookies.get('session_token', '')
    data = handle(cookie_value)
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})

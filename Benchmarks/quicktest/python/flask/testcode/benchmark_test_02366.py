# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest02366():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    os.seteuid(65534)
    return jsonify({"result": "success"})

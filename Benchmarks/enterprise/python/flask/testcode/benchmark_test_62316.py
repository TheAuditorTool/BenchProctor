# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest62316():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200

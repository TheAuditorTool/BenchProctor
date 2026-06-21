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

def BenchmarkTest48864():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200

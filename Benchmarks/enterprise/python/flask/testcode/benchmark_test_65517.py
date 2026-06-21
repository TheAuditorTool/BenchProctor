# SPDX-License-Identifier: Apache-2.0
import random
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest65517():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    processed = data[:64]
    random.seed(int(processed) if str(processed).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200

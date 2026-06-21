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

def BenchmarkTest71680():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    random.seed(int(data) if str(data).isdigit() else 42)
    token = str(random.random())
    return jsonify({'token': str(token)}), 200

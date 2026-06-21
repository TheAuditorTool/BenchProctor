# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import re


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest64083():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})

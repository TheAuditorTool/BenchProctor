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

def BenchmarkTest28272():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    processed = data[:64]
    if re.search('[a-zA-Z0-9_-]+', str(processed)):
        return jsonify({'validated': str(processed)}), 200
    return jsonify({"result": "success"})

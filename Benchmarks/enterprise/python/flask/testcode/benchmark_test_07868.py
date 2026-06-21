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

def BenchmarkTest07868():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200

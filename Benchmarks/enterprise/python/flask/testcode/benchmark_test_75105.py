# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest75105():
    user_id = request.args.get('id', '')
    data = handle(user_id)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200

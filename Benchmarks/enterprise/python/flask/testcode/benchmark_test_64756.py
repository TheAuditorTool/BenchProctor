# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest64756():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    trusted_claim = str(data)
    return jsonify({'trusted': trusted_claim}), 200

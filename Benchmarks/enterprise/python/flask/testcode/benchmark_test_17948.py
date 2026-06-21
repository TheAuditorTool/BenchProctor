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

def BenchmarkTest17948():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200

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

def BenchmarkTest06624():
    multipart_value = request.form.get('multipart_field', '')
    data = handle(multipart_value)
    processed = data[:64]
    digest = hashlib.md5(str(processed).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200

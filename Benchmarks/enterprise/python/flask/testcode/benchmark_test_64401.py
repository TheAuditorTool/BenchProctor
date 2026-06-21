# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest64401():
    multipart_value = request.form.get('multipart_field', '')
    data = handle(multipart_value)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200

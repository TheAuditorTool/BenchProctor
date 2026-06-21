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

def BenchmarkTest47558():
    auth_header = request.headers.get('Authorization', '')
    data = handle(auth_header)
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200

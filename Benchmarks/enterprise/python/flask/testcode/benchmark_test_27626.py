# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest27626():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    processed = data[:64]
    trusted_claim = str(processed)
    return jsonify({'trusted': trusted_claim}), 200

# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest47012(path_param):
    path_value = path_param
    data = handle(path_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200

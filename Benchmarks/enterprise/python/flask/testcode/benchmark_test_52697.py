# SPDX-License-Identifier: Apache-2.0
from flask import jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest52697(path_param):
    path_value = path_param
    data = handle(path_value)
    return jsonify({'error': 'An internal error occurred'}), 500

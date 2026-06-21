# SPDX-License-Identifier: Apache-2.0
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest70666():
    origin_value = request.headers.get('Origin', '')
    data = handle(origin_value)
    return '<html><body><h1>' + str(data) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}

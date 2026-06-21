# SPDX-License-Identifier: Apache-2.0
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest09133():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    return str(data), 200, {'Content-Type': 'text/html'}

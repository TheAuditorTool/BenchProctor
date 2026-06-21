# SPDX-License-Identifier: Apache-2.0
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest17685():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    return str(data), 200, {'Content-Type': 'text/html'}

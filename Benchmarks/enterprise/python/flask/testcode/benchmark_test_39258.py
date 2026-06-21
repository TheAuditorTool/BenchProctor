# SPDX-License-Identifier: Apache-2.0
from flask import request


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest39258():
    upload_name = request.files['upload'].filename
    data = handle(upload_name)
    return str(data), 200, {'Content-Type': 'text/html'}

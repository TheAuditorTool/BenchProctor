# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest78450():
    header_value = request.headers.get('X-Custom-Header', '')
    data = handle(header_value)
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

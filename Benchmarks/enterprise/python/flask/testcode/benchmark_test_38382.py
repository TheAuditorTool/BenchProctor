# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest38382():
    xml_value = request.get_data(as_text=True)
    data = handle(xml_value)
    return jsonify({'error': 'An internal error occurred'}), 500

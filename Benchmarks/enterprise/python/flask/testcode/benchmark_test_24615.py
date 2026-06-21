# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest24615():
    xml_value = request.get_data(as_text=True)
    data = handle(xml_value)
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200

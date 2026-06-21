# SPDX-License-Identifier: Apache-2.0
import html
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest41360():
    multipart_value = request.form.get('multipart_field', '')
    data = handle(multipart_value)
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}

# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest46819():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    if not re.fullmatch('^[\\w\\s.\\-:/=\\r\\n]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<html><body><h1>' + str(processed) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}

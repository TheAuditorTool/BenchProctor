# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest57562():
    header_value = request.headers.get('X-Custom-Header', '')
    data = relay_value(header_value)
    return jsonify({'error': 'An internal error occurred'}), 500

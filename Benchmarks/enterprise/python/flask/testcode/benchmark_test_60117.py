# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60117():
    header_value = request.headers.get('X-Custom-Header', '')
    def normalize(value):
        return value.strip()
    data = normalize(header_value)
    return jsonify({'error': 'An internal error occurred'}), 500

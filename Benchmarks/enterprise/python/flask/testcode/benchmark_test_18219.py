# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18219():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    return jsonify({'error': 'An internal error occurred'}), 500

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03235():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = str(header_value).split(',')
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

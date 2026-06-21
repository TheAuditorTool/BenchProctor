# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39649():
    header_value = request.headers.get('X-Custom-Header', '')
    parts = []
    for token in str(header_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

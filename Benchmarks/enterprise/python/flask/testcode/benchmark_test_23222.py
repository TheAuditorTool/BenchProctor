# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest23222():
    origin_value = request.headers.get('Origin', '')
    parts = []
    for token in str(origin_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

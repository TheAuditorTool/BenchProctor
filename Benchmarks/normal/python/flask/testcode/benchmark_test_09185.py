# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09185():
    ua_value = request.headers.get('User-Agent', '')
    parts = []
    for token in str(ua_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

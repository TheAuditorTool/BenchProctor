# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25657():
    host_value = request.headers.get('Host', '')
    parts = []
    for token in str(host_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

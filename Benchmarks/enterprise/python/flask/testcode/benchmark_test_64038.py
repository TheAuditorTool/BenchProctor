# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64038():
    referer_value = request.headers.get('Referer', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

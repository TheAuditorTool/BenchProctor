# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68225():
    auth_header = request.headers.get('Authorization', '')
    parts = []
    for token in str(auth_header).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

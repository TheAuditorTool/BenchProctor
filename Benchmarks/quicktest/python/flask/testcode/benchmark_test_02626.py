# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02626():
    raw_body = request.get_data(as_text=True)
    parts = []
    for token in str(raw_body).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

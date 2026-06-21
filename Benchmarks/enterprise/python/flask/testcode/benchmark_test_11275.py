# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11275():
    user_id = request.args.get('id', '')
    parts = []
    for token in str(user_id).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13230():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

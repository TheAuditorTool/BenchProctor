# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest80794():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    parts = []
    for token in str(graphql_var).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    return jsonify({'error': 'An internal error occurred'}), 500

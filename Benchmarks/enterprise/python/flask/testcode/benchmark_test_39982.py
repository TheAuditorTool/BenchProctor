# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39982():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    return jsonify({'error': 'An internal error occurred'}), 500

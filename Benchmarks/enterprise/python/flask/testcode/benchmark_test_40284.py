# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest40284():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    return jsonify({'error': 'An internal error occurred'}), 500

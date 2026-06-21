# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest21864():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    return jsonify({'error': 'An internal error occurred'}), 500

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72655():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(graphql_var)
    data = collected
    processed = data[:64]
    return jsonify({'error': str(processed), 'stack': repr(locals())}), 500

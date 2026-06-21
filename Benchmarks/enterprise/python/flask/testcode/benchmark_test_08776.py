# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08776():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = graphql_var
            data = parsed
        case _:
            data = graphql_var
    return jsonify({'error': 'An internal error occurred'}), 500

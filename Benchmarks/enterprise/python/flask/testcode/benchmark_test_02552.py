# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest02552():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    kind = 'json' if str(graphql_var).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = graphql_var
            data = parsed
        case _:
            data = graphql_var
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}

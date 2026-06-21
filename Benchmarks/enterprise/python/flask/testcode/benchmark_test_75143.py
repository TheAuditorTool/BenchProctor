# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest75143():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return str(processed), 200, {'Content-Type': 'text/html'}

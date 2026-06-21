# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04844():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    parts = str(graphql_var).split(',')
    data = ','.join(parts)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}

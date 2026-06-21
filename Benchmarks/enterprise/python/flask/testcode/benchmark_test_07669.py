# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07669():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}

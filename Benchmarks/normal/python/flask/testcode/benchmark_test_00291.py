# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00291():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

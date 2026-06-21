# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61006():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = graphql_var if graphql_var else 'default'
    return jsonify({'error': 'An internal error occurred'}), 500

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79823():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % (graphql_var,)
    return jsonify({'error': 'An internal error occurred'}), 500

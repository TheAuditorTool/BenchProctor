# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72952():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

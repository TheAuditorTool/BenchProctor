# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42249():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    return jsonify({'error': str(graphql_var), 'stack': repr(locals())}), 500

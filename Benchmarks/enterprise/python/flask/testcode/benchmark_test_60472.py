# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60472():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

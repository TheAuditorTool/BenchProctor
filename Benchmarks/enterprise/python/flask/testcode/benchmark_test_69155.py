# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69155():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}

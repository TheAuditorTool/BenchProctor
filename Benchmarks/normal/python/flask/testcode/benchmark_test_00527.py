# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00527():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ' '.join(str(graphql_var).split())
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49188():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(graphql_var)}

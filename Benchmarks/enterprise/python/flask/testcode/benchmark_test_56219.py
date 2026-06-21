# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest56219():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data, _sep, _rest = str(graphql_var).partition('\x00')
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}

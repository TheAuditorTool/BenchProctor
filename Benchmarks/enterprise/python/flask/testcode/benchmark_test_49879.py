# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49879():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}

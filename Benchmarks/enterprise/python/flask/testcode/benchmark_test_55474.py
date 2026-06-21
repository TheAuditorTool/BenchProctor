# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55474():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}

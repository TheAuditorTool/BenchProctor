# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19957():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '{}'.format(graphql_var)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

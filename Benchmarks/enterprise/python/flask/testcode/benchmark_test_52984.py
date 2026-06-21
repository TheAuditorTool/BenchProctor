# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest52984():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = relay_value(graphql_var)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

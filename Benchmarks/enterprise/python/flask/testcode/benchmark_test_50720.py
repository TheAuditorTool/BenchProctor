# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest50720():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

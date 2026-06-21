# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13527():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

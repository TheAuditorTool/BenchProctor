# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35835():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = '%s' % (json_value,)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13777():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

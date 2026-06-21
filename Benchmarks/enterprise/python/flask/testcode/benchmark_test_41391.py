# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41391():
    referer_value = request.headers.get('Referer', '')
    data = '%s' % str(referer_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

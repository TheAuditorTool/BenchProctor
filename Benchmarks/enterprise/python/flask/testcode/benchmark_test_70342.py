# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70342():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

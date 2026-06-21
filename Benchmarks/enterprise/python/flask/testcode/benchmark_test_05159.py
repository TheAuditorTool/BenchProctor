# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05159():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

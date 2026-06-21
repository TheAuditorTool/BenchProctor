# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59374():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

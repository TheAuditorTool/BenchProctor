# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest19580():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

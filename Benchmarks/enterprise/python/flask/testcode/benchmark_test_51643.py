# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51643():
    header_value = request.headers.get('X-Custom-Header', '')
    match str(header_value):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

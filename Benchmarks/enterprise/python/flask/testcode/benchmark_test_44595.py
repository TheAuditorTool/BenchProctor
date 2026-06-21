# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44595():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

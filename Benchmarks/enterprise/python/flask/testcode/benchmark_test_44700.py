# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest44700():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % str(header_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

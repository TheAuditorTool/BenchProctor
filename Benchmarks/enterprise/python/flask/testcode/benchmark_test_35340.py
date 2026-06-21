# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35340():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

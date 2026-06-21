# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest13772():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    parts = str(forwarded_ip).split(',')
    data = ','.join(parts)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

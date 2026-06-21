# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest67389():
    auth_header = request.headers.get('Authorization', '')
    data, _sep, _rest = str(auth_header).partition('\x00')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

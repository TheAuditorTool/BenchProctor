# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20889():
    origin_value = request.headers.get('Origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

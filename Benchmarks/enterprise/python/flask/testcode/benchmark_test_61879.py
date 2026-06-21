# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61879():
    host_value = request.headers.get('Host', '')
    data = str(host_value).replace('\x00', '')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

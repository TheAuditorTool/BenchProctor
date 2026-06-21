# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest00595():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

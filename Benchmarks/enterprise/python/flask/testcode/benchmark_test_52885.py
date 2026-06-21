# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52885():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

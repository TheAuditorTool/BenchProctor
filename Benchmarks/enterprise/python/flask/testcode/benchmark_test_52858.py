# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52858():
    host_value = request.headers.get('Host', '')
    data = f'{host_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

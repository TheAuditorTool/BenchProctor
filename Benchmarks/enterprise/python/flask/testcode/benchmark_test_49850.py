# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest49850():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

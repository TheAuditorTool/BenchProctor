# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33212():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

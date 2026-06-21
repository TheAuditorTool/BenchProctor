# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest54263():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

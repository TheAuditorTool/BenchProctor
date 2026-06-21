# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08210():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

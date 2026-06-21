# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest32193():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

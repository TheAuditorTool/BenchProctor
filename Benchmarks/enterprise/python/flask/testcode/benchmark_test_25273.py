# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25273():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

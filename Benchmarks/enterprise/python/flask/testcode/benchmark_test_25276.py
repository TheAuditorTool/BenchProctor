# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25276():
    referer_value = request.headers.get('Referer', '')
    parts = []
    for token in str(referer_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

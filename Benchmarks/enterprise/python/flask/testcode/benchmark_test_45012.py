# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45012():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

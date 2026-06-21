# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest72115():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

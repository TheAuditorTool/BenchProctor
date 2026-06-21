# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39874():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % str(cookie_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

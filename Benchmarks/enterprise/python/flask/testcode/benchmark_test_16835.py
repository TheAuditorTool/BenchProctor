# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest16835():
    cookie_value = request.cookies.get('session_token', '')
    data = cookie_value if cookie_value else 'default'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest69575():
    cookie_value = request.cookies.get('session_token', '')
    match str(cookie_value):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

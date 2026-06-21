# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70918():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
        case _: action = 'unknown'
    return jsonify({'action': action}), 200

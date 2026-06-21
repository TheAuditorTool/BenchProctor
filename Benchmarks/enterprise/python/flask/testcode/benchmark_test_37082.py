# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37082():
    cookie_value = request.cookies.get('session_token', '')
    data = str(cookie_value).replace('\x00', '')
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

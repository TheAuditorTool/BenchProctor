# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43321():
    cookie_value = request.cookies.get('session_token', '')
    data = (lambda v: v.strip())(cookie_value)
    match str(data):
        case 'a': action = 'alpha'
        case 'b': action = 'beta'
    return jsonify({'action': action}), 200

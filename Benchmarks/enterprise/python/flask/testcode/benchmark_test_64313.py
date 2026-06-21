# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64313():
    cookie_value = request.cookies.get('session_token', '')
    data = '{}'.format(cookie_value)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

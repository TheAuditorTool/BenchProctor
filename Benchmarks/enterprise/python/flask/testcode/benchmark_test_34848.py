# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34848():
    cookie_value = request.cookies.get('session_token', '')
    parts = str(cookie_value).split(',')
    data = ','.join(parts)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

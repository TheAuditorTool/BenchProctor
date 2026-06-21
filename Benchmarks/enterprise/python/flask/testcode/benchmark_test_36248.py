# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36248():
    cookie_value = request.cookies.get('session_token', '')
    data = ' '.join(str(cookie_value).split())
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

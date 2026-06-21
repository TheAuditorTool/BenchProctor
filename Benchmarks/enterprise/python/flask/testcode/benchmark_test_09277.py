# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09277():
    cookie_value = request.cookies.get('session_token', '')
    prefix = ''
    data = prefix + str(cookie_value)
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

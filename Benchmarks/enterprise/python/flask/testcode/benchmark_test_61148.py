# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61148():
    cookie_value = request.cookies.get('session_token', '')
    if str(cookie_value) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

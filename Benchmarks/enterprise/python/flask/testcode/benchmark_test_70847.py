# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest70847():
    cookie_value = request.cookies.get('session_token', '')
    data = f'{cookie_value:.200s}'
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest12085():
    auth_header = request.headers.get('Authorization', '')
    if auth_check('user', str(auth_header)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest13540():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    if auth_check('user', str(forwarded_ip)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

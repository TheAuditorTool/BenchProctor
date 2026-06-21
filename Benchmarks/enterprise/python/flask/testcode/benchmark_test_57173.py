# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest57173():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

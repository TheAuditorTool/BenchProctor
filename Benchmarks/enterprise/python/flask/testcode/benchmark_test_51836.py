# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest51836():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    auth_check('user', data)
    return jsonify({"result": "success"})

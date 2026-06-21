# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest28225():
    header_value = request.headers.get('X-Custom-Header', '')
    if auth_check('user', str(header_value)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

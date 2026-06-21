# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest28007():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})

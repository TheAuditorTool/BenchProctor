# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest05538():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})

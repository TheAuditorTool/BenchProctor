# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest77098():
    host_value = request.headers.get('Host', '')
    data = host_value if host_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})

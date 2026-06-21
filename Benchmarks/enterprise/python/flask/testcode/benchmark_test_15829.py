# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest15829():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

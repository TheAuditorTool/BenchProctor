# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest13386():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    auth_check('user', forwarded_ip)
    return jsonify({"result": "success"})

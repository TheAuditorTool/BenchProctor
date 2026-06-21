# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest03891():
    host_value = request.headers.get('Host', '')
    auth_check('user', host_value)
    return jsonify({"result": "success"})

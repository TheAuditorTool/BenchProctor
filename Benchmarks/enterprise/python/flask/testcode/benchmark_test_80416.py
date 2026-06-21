# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest80416():
    referer_value = request.headers.get('Referer', '')
    auth_check('user', referer_value)
    return jsonify({"result": "success"})

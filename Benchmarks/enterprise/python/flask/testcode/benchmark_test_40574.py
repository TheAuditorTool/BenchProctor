# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest40574():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    auth_check('user', data)
    return jsonify({"result": "success"})

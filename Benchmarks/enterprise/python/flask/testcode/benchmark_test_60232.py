# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest60232():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

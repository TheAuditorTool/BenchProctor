# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest15177():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})

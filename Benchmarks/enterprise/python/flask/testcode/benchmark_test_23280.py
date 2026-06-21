# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest23280():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    auth_check('user', data)
    return jsonify({"result": "success"})

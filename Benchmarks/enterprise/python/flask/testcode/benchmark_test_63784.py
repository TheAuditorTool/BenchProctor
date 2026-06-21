# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest63784():
    origin_value = request.headers.get('Origin', '')
    data = '{}'.format(origin_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

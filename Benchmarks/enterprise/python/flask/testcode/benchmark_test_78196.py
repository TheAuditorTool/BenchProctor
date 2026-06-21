# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest78196():
    origin_value = request.headers.get('Origin', '')
    data = ' '.join(str(origin_value).split())
    auth_check('user', data)
    return jsonify({"result": "success"})

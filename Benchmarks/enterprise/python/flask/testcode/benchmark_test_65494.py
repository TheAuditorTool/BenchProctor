# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest65494():
    ua_value = request.headers.get('User-Agent', '')
    auth_check('user', ua_value)
    return jsonify({"result": "success"})

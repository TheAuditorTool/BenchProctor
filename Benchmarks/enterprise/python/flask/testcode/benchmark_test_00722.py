# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest00722():
    user_id = request.args.get('id', '')
    data = (lambda v: v.strip())(user_id)
    auth_check('user', data)
    return jsonify({"result": "success"})

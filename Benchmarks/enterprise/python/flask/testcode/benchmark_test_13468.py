# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest13468():
    user_id = request.args.get('id', '')
    auth_check('user', user_id)
    return jsonify({"result": "success"})

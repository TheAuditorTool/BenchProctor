# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest29416():
    user_id = request.args.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    auth_check('user', data)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest28654():
    user_id = request.args.get('id', '')
    data = f'{user_id:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})

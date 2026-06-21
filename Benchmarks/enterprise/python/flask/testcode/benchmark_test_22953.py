# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def ensure_str(value):
    return str(value)

def BenchmarkTest22953():
    user_id = request.args.get('id', '')
    data = ensure_str(user_id)
    auth_check('user', data)
    return jsonify({"result": "success"})

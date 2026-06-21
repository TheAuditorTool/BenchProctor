# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest10583():
    user_id = request.args.get('id', '')
    data = default_blank(user_id)
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

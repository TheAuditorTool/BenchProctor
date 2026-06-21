# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest04443():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    attempts = globals().setdefault('_login_attempts', {})
    attempts['user'] = attempts.get('user', 0) + 1
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest54538():
    upload_name = request.files['upload'].filename
    if auth_check('user', str(upload_name)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

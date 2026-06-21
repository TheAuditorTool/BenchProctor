# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest00978():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    auth_check('user', data)
    return jsonify({"result": "success"})

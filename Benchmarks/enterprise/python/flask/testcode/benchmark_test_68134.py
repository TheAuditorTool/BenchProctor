# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest68134():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})

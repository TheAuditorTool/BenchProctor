# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest42880():
    upload_name = request.files['upload'].filename
    auth_check('user', upload_name)
    return jsonify({"result": "success"})

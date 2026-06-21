# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest63411():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    auth_check('user', data)
    return jsonify({"result": "success"})

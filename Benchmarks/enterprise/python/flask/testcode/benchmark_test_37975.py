# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest37975():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    auth_check('user', data)
    return jsonify({"result": "success"})

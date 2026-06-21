# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest47530():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    auth_check('user', data)
    return jsonify({"result": "success"})

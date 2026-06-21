# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest23076():
    upload_name = request.files['upload'].filename
    data, _sep, _rest = str(upload_name).partition('\x00')
    auth_check('user', data)
    return jsonify({"result": "success"})

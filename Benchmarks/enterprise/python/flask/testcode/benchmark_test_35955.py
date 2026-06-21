# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest35955():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest60046():
    upload_name = request.files['upload'].filename
    data = '%s' % (upload_name,)
    auth_check('user', data)
    return jsonify({"result": "success"})

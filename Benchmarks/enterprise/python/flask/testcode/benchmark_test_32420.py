# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest32420():
    multipart_value = request.form.get('multipart_field', '')
    if auth_check('user', str(multipart_value)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

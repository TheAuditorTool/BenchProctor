# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest26843():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

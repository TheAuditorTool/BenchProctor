# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest19877():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = str(ast.literal_eval(multipart_value))
    except (ValueError, SyntaxError):
        data = multipart_value
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return jsonify({"result": "success"})

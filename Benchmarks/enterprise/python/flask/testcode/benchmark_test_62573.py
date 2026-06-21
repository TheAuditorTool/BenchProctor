# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest62573():
    upload_name = request.files['upload'].filename
    try:
        data = str(ast.literal_eval(upload_name))
    except (ValueError, SyntaxError):
        data = upload_name
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})

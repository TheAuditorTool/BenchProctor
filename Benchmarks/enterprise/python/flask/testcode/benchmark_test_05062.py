# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import ast
from app_runtime import auth_check


def BenchmarkTest05062():
    field_value = request.form.get('field', '')
    try:
        data = str(ast.literal_eval(field_value))
    except (ValueError, SyntaxError):
        data = field_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})

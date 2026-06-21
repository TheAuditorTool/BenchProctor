# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request, jsonify
import os
import ast


def BenchmarkTest19768():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    if os.environ.get("APP_ENV", "production") != "test":
        return redirect(str(data))
    return jsonify({"result": "success"})

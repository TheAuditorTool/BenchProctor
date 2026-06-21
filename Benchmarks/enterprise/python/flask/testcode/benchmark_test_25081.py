# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import os
import ast


def BenchmarkTest25081():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    if os.environ.get("APP_ENV", "production") != "test":
        return render_template_string(data)
    return jsonify({"result": "success"})

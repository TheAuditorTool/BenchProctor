# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import os
import ast


def BenchmarkTest64173():
    cookie_value = request.cookies.get('session_token', '')
    try:
        data = str(ast.literal_eval(cookie_value))
    except (ValueError, SyntaxError):
        data = cookie_value
    if os.environ.get("APP_ENV", "production") != "test":
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})

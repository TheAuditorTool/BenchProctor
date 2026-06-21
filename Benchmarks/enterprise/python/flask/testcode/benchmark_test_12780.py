# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import os
import ast


def BenchmarkTest12780():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    if os.environ.get("APP_ENV", "production") != "test":
        return Markup('<img src="' + str(data) + '">')
    return jsonify({"result": "success"})

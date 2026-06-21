# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import ast
from app_runtime import db


def BenchmarkTest76713():
    host_value = request.headers.get('Host', '')
    try:
        data = str(ast.literal_eval(host_value))
    except (ValueError, SyntaxError):
        data = host_value
    if os.environ.get("APP_ENV", "production") != "test":
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})

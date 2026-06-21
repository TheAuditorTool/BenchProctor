# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import ast
from app_runtime import db


def BenchmarkTest15657():
    header_value = request.headers.get('X-Custom-Header', '')
    try:
        data = str(ast.literal_eval(header_value))
    except (ValueError, SyntaxError):
        data = header_value
    if time.time() > 1000000000:
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    return jsonify({"result": "success"})

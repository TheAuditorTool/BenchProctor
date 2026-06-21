# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
from app_runtime import db


def BenchmarkTest63595():
    origin_value = request.headers.get('Origin', '')
    try:
        data = str(ast.literal_eval(origin_value))
    except (ValueError, SyntaxError):
        data = origin_value
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(data),))
    return jsonify({"result": "success"})

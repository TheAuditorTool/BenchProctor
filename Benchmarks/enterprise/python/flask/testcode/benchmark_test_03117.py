# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
from app_runtime import db


def BenchmarkTest03117():
    raw_body = request.get_data(as_text=True)
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    db.execute('SELECT * FROM users WHERE id = ?', (data,))
    return jsonify({"result": "success"})

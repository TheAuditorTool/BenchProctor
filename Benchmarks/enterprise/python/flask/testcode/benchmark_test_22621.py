# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest22621():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

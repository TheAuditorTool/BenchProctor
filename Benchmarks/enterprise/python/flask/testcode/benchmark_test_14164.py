# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest14164():
    db_value = db.fetch_one('SELECT name FROM users LIMIT 1')
    try:
        data = str(ast.literal_eval(db_value))
    except (ValueError, SyntaxError):
        data = db_value
    processed = data[:64]
    if str(processed) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})

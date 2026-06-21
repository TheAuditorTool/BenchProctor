# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast
from app_runtime import db, auth_check


def BenchmarkTest18733():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    auth_check('user', data)
    return jsonify({"result": "success"})

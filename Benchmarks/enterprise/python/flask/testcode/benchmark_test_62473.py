# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
import ast
from app_runtime import db, auth_check


def BenchmarkTest62473():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})

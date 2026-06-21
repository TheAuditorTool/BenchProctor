# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest62859():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200

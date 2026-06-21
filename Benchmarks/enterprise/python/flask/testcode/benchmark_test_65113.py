# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest65113():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200

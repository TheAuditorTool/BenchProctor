# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest00454():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500

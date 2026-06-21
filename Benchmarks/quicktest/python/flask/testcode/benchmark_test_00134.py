# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import re
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest00134():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)

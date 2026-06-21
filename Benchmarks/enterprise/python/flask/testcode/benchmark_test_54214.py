# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
import ast
from app_runtime import db


def BenchmarkTest54214():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest18285():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    eval(compile('yaml.load(data, Loader=yaml.UnsafeLoader)', '<sink>', 'exec'))
    return jsonify({"result": "success"})

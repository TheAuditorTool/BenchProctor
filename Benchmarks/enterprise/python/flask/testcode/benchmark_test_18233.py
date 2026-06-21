# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest18233():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    if os.environ.get("APP_ENV", "production") != "test":
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})

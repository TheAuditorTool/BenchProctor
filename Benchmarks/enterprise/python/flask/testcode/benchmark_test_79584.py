# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest79584():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    requests.post('http://api.prod.internal/data', data=str(data))
    return jsonify({"result": "success"})

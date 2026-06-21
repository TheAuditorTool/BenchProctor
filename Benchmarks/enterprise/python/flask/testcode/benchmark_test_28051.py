# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import ast
from app_runtime import db


def BenchmarkTest28051():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = str(ast.literal_eval(comment_value))
    except (ValueError, SyntaxError):
        data = comment_value
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return jsonify({"result": "success"})

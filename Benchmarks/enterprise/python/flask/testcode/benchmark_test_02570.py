# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
from app_runtime import db, auth_check


def BenchmarkTest02570():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    auth_check('user', data)
    return jsonify({"result": "success"})

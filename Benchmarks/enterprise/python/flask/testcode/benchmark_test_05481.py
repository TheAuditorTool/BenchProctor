# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest05481():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    session['user'] = str(data)
    return jsonify({"result": "success"})

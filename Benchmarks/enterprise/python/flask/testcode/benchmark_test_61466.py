# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
import json
from app_runtime import db, auth_check


def BenchmarkTest61466():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})

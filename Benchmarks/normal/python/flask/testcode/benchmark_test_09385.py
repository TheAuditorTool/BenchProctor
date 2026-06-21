# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
import json
from app_runtime import db


def BenchmarkTest09385():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        data = json.loads(comment_value).get('value', comment_value)
    except (json.JSONDecodeError, AttributeError):
        data = comment_value
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


def to_text(value):
    return str(value).strip()

def BenchmarkTest65876():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = to_text(comment_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

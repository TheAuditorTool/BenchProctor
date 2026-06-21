# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db, auth_check


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest04259():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = default_blank(comment_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

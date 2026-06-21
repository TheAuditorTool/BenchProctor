# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest03515():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    db.execute('UPDATE users SET role = ? WHERE id = 1', (str(comment_value),))
    return jsonify({"result": "success"})

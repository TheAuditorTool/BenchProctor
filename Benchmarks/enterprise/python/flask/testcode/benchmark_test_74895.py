# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest74895():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    db.execute('SELECT * FROM users WHERE id = ?', (comment_value,))
    return jsonify({"result": "success"})

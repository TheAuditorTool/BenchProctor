# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest15378():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if len(str(comment_value)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

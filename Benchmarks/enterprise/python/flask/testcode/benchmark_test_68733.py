# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest68733():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    if str(comment_value).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

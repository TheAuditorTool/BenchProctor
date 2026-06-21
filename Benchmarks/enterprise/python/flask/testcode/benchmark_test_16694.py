# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest16694():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    arr = [10, 20, 30, 40, 50]
    idx = int(str(comment_value))
    return jsonify({'lookup': arr[idx]}), 200

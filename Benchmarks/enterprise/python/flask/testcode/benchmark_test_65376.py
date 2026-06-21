# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import db


def BenchmarkTest65376():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    try:
        result = int(str(comment_value))
    except Exception:
        pass
    return jsonify({"result": "success"})
